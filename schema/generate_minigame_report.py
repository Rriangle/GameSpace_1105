import datetime
import re
from collections import OrderedDict
from decimal import Decimal
from pathlib import Path
from typing import List, Dict, Any

import pyodbc


BASE_DIR = Path(__file__).resolve().parent
STRUCTURE_DOC = BASE_DIR / "MiniGame_Area_資料庫架構完整文檔_2025-11-05.md"
OUTPUT_PATH = BASE_DIR / "MiniGameArea_DB架構與種子資料報告.md"

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-8HQIS1S\\SQLEXPRESS;"
    "DATABASE=GameSpacedatabase;"
    "Trusted_Connection=yes;"
)

TABLE_CATEGORIES = [
    {
        "title": "使用者／權限相關表格（完整列出全部種子）",
        "tables": [
            {"name": "Users", "schema": "dbo", "order_by": "User_ID", "seed_mode": "all"},
            {"name": "ManagerData", "schema": "dbo", "order_by": "Manager_Id", "seed_mode": "all"},
            {
                "name": "ManagerRolePermission",
                "schema": "dbo",
                "order_by": "ManagerRole_Id",
                "seed_mode": "all",
            },
            {
                "name": "ManagerRole",
                "schema": "dbo",
                "order_by": "Manager_Id, ManagerRole_Id",
                "seed_mode": "all",
            },
        ],
    },
    {
        "title": "MiniGame Area 定義／規則／設定類表格（完整列出全部種子）",
        "tables": [
            {"name": "CouponType", "schema": "dbo", "order_by": "CouponTypeID", "seed_mode": "all"},
            {"name": "EVoucherType", "schema": "dbo", "order_by": "EVoucherTypeID", "seed_mode": "all"},
            {
                "name": "PetBackgroundCostSettings",
                "schema": "dbo",
                "order_by": "DisplayOrder, BackgroundCode",
                "seed_mode": "all",
            },
            {
                "name": "PetSkinColorCostSettings",
                "schema": "dbo",
                "order_by": "DisplayOrder, ColorCode",
                "seed_mode": "all",
            },
            {
                "name": "PetLevelRewardSettings",
                "schema": "dbo",
                "order_by": "LevelRangeStart, LevelRangeEnd",
                "seed_mode": "all",
            },
            {"name": "SignInRule", "schema": "dbo", "order_by": "SignInDay", "seed_mode": "all"},
            {"name": "SystemSettings", "schema": "dbo", "order_by": "SettingId", "seed_mode": "all"},
        ],
    },
    {
        "title": "MiniGame Area 使用者相關表格（僅列出 UserID 10000001 與 10000002）",
        "tables": [
            {
                "name": "Coupon",
                "schema": "dbo",
                "order_by": "UserID, CouponID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "EVoucher",
                "schema": "dbo",
                "order_by": "UserID, EVoucherID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "EVoucherToken",
                "schema": "dbo",
                "order_by": "TokenID",
                "seed_mode": "filter",
                "seed_filter": (
                    "EVoucherID IN (SELECT EVoucherID FROM dbo.EVoucher "
                    "WHERE UserID IN (10000001, 10000002))"
                ),
                "seed_note": "EVoucher 所屬 UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "EVoucherRedeemLog",
                "schema": "dbo",
                "order_by": "UserID, RedeemID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "MiniGame",
                "schema": "dbo",
                "order_by": "UserID, PlayID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "Pet",
                "schema": "dbo",
                "order_by": "UserID, PetID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "User_Wallet",
                "schema": "dbo",
                "order_by": "User_Id",
                "seed_mode": "filter",
                "seed_filter": "User_Id IN (10000001, 10000002)",
                "seed_note": "User_Id ∈ {10000001, 10000002}",
            },
            {
                "name": "UserSignInStats",
                "schema": "dbo",
                "order_by": "UserID, LogID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
            {
                "name": "WalletHistory",
                "schema": "dbo",
                "order_by": "UserID, LogID",
                "seed_mode": "filter",
                "seed_filter": "UserID IN (10000001, 10000002)",
                "seed_note": "UserID ∈ {10000001, 10000002}",
            },
        ],
    },
]


def load_structure_document() -> str:
    if not STRUCTURE_DOC.exists():
        return ""
    return STRUCTURE_DOC.read_text(encoding="utf-8")


STRUCTURE_TEXT = load_structure_document()


def get_purpose(table_name: str) -> str:
    if not STRUCTURE_TEXT:
        return ""
    pattern = re.compile(
        rf"### [^\n]*{re.escape(table_name)}[^\n]*\n\n\*\*用途\*\*: ([^\n]+)", re.MULTILINE
    )
    match = pattern.search(STRUCTURE_TEXT)
    if match:
        return match.group(1).strip()
    return ""


def clean_default(definition: str) -> str:
    if not definition:
        return ""
    value = definition.strip()
    while value.startswith("(") and value.endswith(")"):
        value = value[1:-1].strip()
    return value


def format_data_type(row: pyodbc.Row) -> str:
    data_type = row.data_type
    max_length = row.max_length
    precision = row.precision
    scale = row.scale

    if data_type in {"nvarchar", "nchar"}:
        if max_length == -1:
            length = "max"
        else:
            length = str(max_length // 2)
        return f"{data_type}({length})"
    if data_type in {"varchar", "char", "varbinary", "binary"}:
        if max_length == -1:
            length = "max"
        else:
            length = str(max_length)
        return f"{data_type}({length})"
    if data_type in {"decimal", "numeric"}:
        return f"{data_type}({precision},{scale})"
    if data_type in {"datetime2", "datetimeoffset", "time"}:
        return f"{data_type}({scale})"
    if data_type == "float":
        return "float"
    return data_type


def fetch_columns(cursor: pyodbc.Cursor, schema: str, table: str) -> List[Dict[str, Any]]:
    query = """
        SELECT c.column_id,
               c.name AS column_name,
               t.name AS data_type,
               c.max_length,
               c.precision,
               c.scale,
               c.is_nullable,
               c.is_identity,
               c.is_computed,
               dc.definition AS default_definition,
               CAST(ic.seed_value AS NVARCHAR(50)) AS seed_value,
               CAST(ic.increment_value AS NVARCHAR(50)) AS increment_value
        FROM sys.columns c
        JOIN sys.types t
             ON c.user_type_id = t.user_type_id
            AND t.user_type_id = t.system_type_id
        LEFT JOIN sys.default_constraints dc
             ON c.default_object_id = dc.object_id
        LEFT JOIN sys.identity_columns ic
             ON c.object_id = ic.object_id
            AND c.column_id = ic.column_id
        WHERE c.object_id = OBJECT_ID(?)
        ORDER BY c.column_id;
    """
    cursor.execute(query, f"[{schema}].[{table}]")
    result = []
    for row in cursor.fetchall():
        result.append(
            {
                "column_name": row.column_name,
                "data_type": format_data_type(row),
                "is_nullable": "YES" if row.is_nullable else "NO",
                "default": clean_default(row.default_definition),
                "is_identity": bool(row.is_identity),
                "identity_seed": row.seed_value,
                "identity_increment": row.increment_value,
                "is_computed": bool(row.is_computed),
            }
        )
    return result


def fetch_indexes(cursor: pyodbc.Cursor, schema: str, table: str) -> List[Dict[str, Any]]:
    query = """
        SELECT i.name,
               i.is_primary_key,
               i.is_unique_constraint,
               i.is_unique,
               i.type_desc,
               c.name AS column_name,
               ic.key_ordinal,
               i.has_filter,
               i.filter_definition
        FROM sys.indexes i
        JOIN sys.index_columns ic
             ON i.object_id = ic.object_id
            AND i.index_id = ic.index_id
        JOIN sys.columns c
             ON c.object_id = ic.object_id
            AND c.column_id = ic.column_id
        WHERE i.object_id = OBJECT_ID(?)
          AND i.is_hypothetical = 0
        ORDER BY i.index_id, ic.key_ordinal;
    """
    cursor.execute(query, f"[{schema}].[{table}]")
    index_map: OrderedDict[str, Dict[str, Any]] = OrderedDict()
    for row in cursor.fetchall():
        info = index_map.setdefault(
            row.name,
            {
                "name": row.name,
                "is_primary_key": bool(row.is_primary_key),
                "is_unique_constraint": bool(row.is_unique_constraint),
                "is_unique": bool(row.is_unique),
                "type_desc": row.type_desc,
                "has_filter": bool(row.has_filter),
                "filter_definition": row.filter_definition,
                "columns": [],
            },
        )
        info["columns"].append((row.key_ordinal, row.column_name))
    for details in index_map.values():
        details["columns"] = [name for _, name in sorted(details["columns"], key=lambda item: item[0])]
    return list(index_map.values())


def fetch_foreign_keys(cursor: pyodbc.Cursor, schema: str, table: str) -> List[Dict[str, Any]]:
    query = """
        SELECT fk.name,
               COL_NAME(fkc.parent_object_id, fkc.parent_column_id) AS parent_column,
               OBJECT_SCHEMA_NAME(fk.referenced_object_id) AS ref_schema,
               OBJECT_NAME(fk.referenced_object_id) AS ref_table,
               COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS ref_column,
               fk.delete_referential_action_desc AS delete_action,
               fk.update_referential_action_desc AS update_action,
               fkc.constraint_column_id
        FROM sys.foreign_keys fk
        JOIN sys.foreign_key_columns fkc
             ON fk.object_id = fkc.constraint_object_id
        WHERE fk.parent_object_id = OBJECT_ID(?)
        ORDER BY fk.name, fkc.constraint_column_id;
    """
    cursor.execute(query, f"[{schema}].[{table}]")
    fk_map: OrderedDict[str, Dict[str, Any]] = OrderedDict()
    for row in cursor.fetchall():
        info = fk_map.setdefault(
            row.name,
            {
                "name": row.name,
                "ref_table": f"{row.ref_schema}.{row.ref_table}",
                "delete_action": row.delete_action,
                "update_action": row.update_action,
                "pairs": [],
            },
        )
        info["pairs"].append((row.parent_column, row.ref_column))
    return list(fk_map.values())


def fetch_check_constraints(cursor: pyodbc.Cursor, schema: str, table: str) -> List[Dict[str, str]]:
    query = """
        SELECT cc.name, cc.definition
        FROM sys.check_constraints cc
        WHERE cc.parent_object_id = OBJECT_ID(?)
        ORDER BY cc.name;
    """
    cursor.execute(query, f"[{schema}].[{table}]")
    result = []
    for row in cursor.fetchall():
        definition = row.definition.strip()
        result.append({"name": row.name, "definition": definition})
    return result


def fetch_row_count(cursor: pyodbc.Cursor, schema: str, table: str) -> int:
    cursor.execute(f"SELECT COUNT(*) FROM [{schema}].[{table}]")
    return int(cursor.fetchone()[0])


def format_value(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, (int, float, Decimal)):
        return str(value)
    if isinstance(value, datetime.datetime):
        formatted = value.strftime("%Y-%m-%d %H:%M:%S.%f").rstrip("0").rstrip(".")
        return formatted
    if isinstance(value, datetime.date):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, datetime.time):
        return value.strftime("%H:%M:%S.%f").rstrip("0").rstrip(".")
    if isinstance(value, (bytes, bytearray, memoryview)):
        return "0x" + bytes(value).hex().upper()
    text = str(value)
    return text.replace("|", "\\|")


def render_markdown_table(headers: List[str], rows: List[List[Any]]) -> List[str]:
    lines = []
    header_line = "| " + " | ".join(headers) + " |"
    divider_line = "| " + " | ".join(["---"] * len(headers)) + " |"
    lines.append(header_line)
    lines.append(divider_line)
    for row in rows:
        formatted = [format_value(value) for value in row]
        lines.append("| " + " | ".join(formatted) + " |")
    return lines


def fetch_seed_data(
    cursor: pyodbc.Cursor,
    schema: str,
    table: str,
    order_by: str,
    seed_mode: str,
    seed_filter: str = "",
) -> Dict[str, Any]:
    base_query = f"SELECT * FROM [{schema}].[{table}]"
    if seed_mode == "filter" and seed_filter:
        base_query += f" WHERE {seed_filter}"
    if order_by:
        base_query += f" ORDER BY {order_by}"
    cursor.execute(base_query)
    rows = cursor.fetchall()
    headers = [col[0] for col in cursor.description]
    data = [list(row) for row in rows]
    return {"headers": headers, "rows": data, "count": len(data)}


def summarize_indexes(indexes: List[Dict[str, Any]]) -> List[str]:
    pk_lines, unique_lines, other_lines = [], [], []
    for idx in indexes:
        columns = ", ".join(idx["columns"])
        descriptor = f"{idx['name']} ({idx['type_desc']}) → {columns}"
        if idx["has_filter"] and idx["filter_definition"]:
            descriptor += f" | Filter: {idx['filter_definition']}"
        if idx["is_primary_key"]:
            pk_lines.append(descriptor)
        elif idx["is_unique_constraint"]:
            unique_lines.append(descriptor + " (UNIQUE CONSTRAINT)")
        elif idx["is_unique"]:
            unique_lines.append(descriptor + " (UNIQUE INDEX)")
        else:
            other_lines.append(descriptor)
    lines = []
    if pk_lines:
        lines.append("- **主鍵**:")
        for item in pk_lines:
            lines.append(f"  - {item}")
    if unique_lines:
        lines.append("- **唯一性約束／索引**:")
        for item in unique_lines:
            lines.append(f"  - {item}")
    if other_lines:
        lines.append("- **其他索引**:")
        for item in other_lines:
            lines.append(f"  - {item}")
    return lines


def summarize_foreign_keys(foreign_keys: List[Dict[str, Any]]) -> List[str]:
    if not foreign_keys:
        return ["- 無外鍵"]
    lines = []
    for fk in foreign_keys:
        column_pairs = ", ".join(f"{src} → {dst}" for src, dst in fk["pairs"])
        lines.append(
            f"- {fk['name']}: {column_pairs} | 參照 {fk['ref_table']} | "
            f"ON UPDATE {fk['update_action']} / ON DELETE {fk['delete_action']}"
        )
    return lines


def summarize_checks(checks: List[Dict[str, str]]) -> List[str]:
    if not checks:
        return ["- 無 CHECK 約束"]
    return [f"- {check['name']}: {check['definition']}" for check in checks]


def build_table_section(
    cursor: pyodbc.Cursor,
    schema: str,
    table: str,
    order_by: str,
    seed_mode: str,
    seed_filter: str = "",
    seed_note: str = "",
) -> List[str]:
    lines: List[str] = []
    purpose = get_purpose(table)
    columns = fetch_columns(cursor, schema, table)
    indexes = fetch_indexes(cursor, schema, table)
    foreign_keys = fetch_foreign_keys(cursor, schema, table)
    checks = fetch_check_constraints(cursor, schema, table)
    row_count = fetch_row_count(cursor, schema, table)
    seed_data = fetch_seed_data(cursor, schema, table, order_by, seed_mode, seed_filter)

    lines.append(f"### {schema}.{table}")
    if purpose:
        lines.append(f"用途：{purpose}")
    lines.append(f"總筆數（資料庫）：{row_count}")
    lines.append("")

    lines.append("#### 欄位結構")
    column_rows = []
    for col in columns:
        extra_flags = []
        if col["is_identity"]:
            seed = col["identity_seed"] or "1"
            increment = col["identity_increment"] or "1"
            extra_flags.append(f"IDENTITY({seed},{increment})")
        if col["is_computed"]:
            extra_flags.append("COMPUTED")
        extra = ", ".join(extra_flags)
        column_rows.append(
            [
                col["column_name"],
                col["data_type"],
                col["is_nullable"],
                col["default"] or "",
                extra,
            ]
        )
    lines.extend(render_markdown_table(["Column", "Data Type", "Nullable", "Default", "Extra"], column_rows))
    lines.append("")

    lines.append("#### 索引與鍵")
    index_lines = summarize_indexes(indexes)
    if index_lines:
        lines.extend(index_lines)
    else:
        lines.append("- 無索引資訊")
    lines.append("")

    lines.append("#### 外鍵")
    lines.extend(summarize_foreign_keys(foreign_keys))
    lines.append("")

    lines.append("#### CHECK 約束")
    lines.extend(summarize_checks(checks))
    lines.append("")

    lines.append("#### 種子資料")
    if seed_mode == "filter" and seed_note:
        lines.append(f"- 匯出條件：{seed_note}")
    lines.append(f"- 匯出筆數：{seed_data['count']}")
    if seed_mode == "filter":
        lines.append(
            f"- 提醒：其餘筆數已省略（僅列出指定使用者），完整筆數請查詢資料庫。"
        )
    if seed_data["count"] == 0:
        lines.append("（無符合條件的紀錄）")
    else:
        lines.extend(render_markdown_table(seed_data["headers"], seed_data["rows"]))
    lines.append("")
    return lines


def main() -> None:
    report_lines: List[str] = []
    report_lines.append("# MiniGame Area 資料庫架構與種子資料報告")
    report_lines.append("")
    report_lines.append(
        "目的：彙整 GameSpacedatabase 中 MiniGame Area 相關 20 張資料表（含 "
        "使用者／權限表格 4 張），提供欄位結構、索引／約束與指定範圍的種子資料，"
        "讓日後的 AI 任務無須直接連線 SQL Server 即能掌握資料庫設計。"
    )
    report_lines.append("")
    report_lines.append("- SQL Server：DESKTOP-8HQIS1S\\\\SQLEXPRESS")
    report_lines.append("- 資料庫：GameSpacedatabase")
    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    report_lines.append(f"- 生成時間：{timestamp}")
    report_lines.append("- 製作規則：定義／規則／設定表格列出全部種子；其他主表僅列出 UserID 10000001 與 10000002 相關紀錄；使用者／權限表格列出全部種子。")
    report_lines.append("")

    with pyodbc.connect(CONNECTION_STRING) as conn:
        cursor = conn.cursor()
        for category in TABLE_CATEGORIES:
            report_lines.append(f"## {category['title']}")
            report_lines.append("")
            for table_cfg in category["tables"]:
                report_lines.extend(
                    build_table_section(
                        cursor=cursor,
                        schema=table_cfg["schema"],
                        table=table_cfg["name"],
                        order_by=table_cfg.get("order_by", ""),
                        seed_mode=table_cfg.get("seed_mode", "all"),
                        seed_filter=table_cfg.get("seed_filter", ""),
                        seed_note=table_cfg.get("seed_note", ""),
                    )
                )

    OUTPUT_PATH.write_text("\n".join(report_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
