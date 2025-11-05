# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a dual-project ASP.NET Core 8.0 MVC gaming platform consisting of:
- **GameSpace**: Admin backend portal (HTTPS:7042, HTTP:5211)
- **GamiPort**: Public-facing frontend (HTTPS:7160, HTTP:5001)

Both projects share the **GameSpacedatabase** SQL Server database and are organized using ASP.NET Areas for modular development.

## Database Architecture

**Critical**: The database is the single source of truth. Schema modifications via EF Migrations are **strictly prohibited**.

- **Database**: GameSpacedatabase on SQL Server (SQLEXPRESS)
- **Connection String**: Located in `appsettings.json` → `ConnectionStrings:GameSpace` (or `GameSpacedatabase` or `DefaultConnection`)
- **DbContext**: `GameSpacedatabaseContext` (in `Models/` for both projects)
- **Total Tables**: 103 tables across all areas
- **Schema Files**: Reference files in `schema/` directory (for AI reference only)

### MiniGame Area Core Tables (20 tables)
- Wallet: `User_Wallet`, `WalletHistory`, `CouponType`, `Coupon`, `EVoucherType`, `EVoucher`, `EVoucherToken`, `EVoucherRedeemLog`
- Sign-in: `SignInRule`, `UserSignInStats`
- Pet: `Pet`, `PetSkinColorCostSettings`, `PetBackgroundCostSettings`, `PetLevelRewardSettings`
- Game: `MiniGame`
- Config: `SystemSettings` (dynamic configuration center - 36 rules, 30min cache)
- Auth: `Users`, `ManagerData`, `ManagerRole`, `ManagerRolePermission`

## Project Structure

### GameSpace (Admin Backend)
```
GameSpace/GameSpace/
├── Areas/
│   ├── MiniGame/          # 24 controllers, 94 services (COMPLETED)
│   ├── Forum/             # Forum management
│   ├── MemberManagement/  # User management
│   ├── OnlineStore/       # Store administration
│   ├── social_hub/        # Social features + SignalR Hubs
│   └── Identity/          # Identity pages
├── Infrastructure/
│   ├── Login/             # Shared login services
│   └── Time/              # Time utilities (TimeZones.Taipei)
├── Models/                # GameSpacedatabaseContext + entities
├── wwwroot/lib/sb-admin/ # SB Admin template (DO NOT MODIFY)
├── Program.cs             # DI + Middleware (259 lines)
└── appsettings.json
```

### GamiPort (Public Frontend)
```
GamiPort/GamiPort/
├── Areas/
│   ├── MiniGame/          # Client-facing MiniGame features (IN PROGRESS)
│   ├── Forum/             # Forum + API controllers
│   ├── Login/             # Registration + authentication
│   ├── MemberManagement/  # User profiles
│   ├── OnlineStore/       # E-commerce + ECPay integration
│   └── social_hub/        # Chat + SignalR Hubs
├── Infrastructure/
│   ├── Security/          # IAppCurrentUser + AppCurrentUser
│   └── Time/              # Time utilities
├── Models/                # GameSpacedatabaseContext + entities
├── Program.cs             # Pure Cookie auth (no Identity)
└── appsettings.json
```

## Authentication & Authorization

### GameSpace (Admin)
- **Scheme**: `AdminCookie` (Claims-based)
- **Cookie Name**: `AdminCookie`
- **Login Path**: `/Login/Index`
- **Claims**: `IsManager=true`, role/permission claims
- **Authorization**: `[Authorize(AuthenticationSchemes="AdminCookie", Policy="AdminOnly")]`
- **Permission Check**: Via `ManagerData`, `ManagerRole`, `ManagerRolePermission` tables

### GamiPort (Public)
- **Scheme**: `CookieAuthenticationDefaults.AuthenticationScheme`
- **Cookie Name**: `GamiPort.User`
- **Login Path**: `/Login/Login/Login`
- **Current User**: Via `IAppCurrentUser` interface (`Infrastructure/Security/`)
- **Password Hashing**: `IPasswordHasher<User>` / `PasswordHasher<User>`

### CORS Configuration
GamiPort allows cross-origin requests from GameSpace for SignalR support (see `Program.cs` → `SupportCors` policy).

## Key Development Commands

### Build
```bash
# Build specific project
dotnet build GameSpace/GameSpace/GameSpace.csproj
dotnet build GamiPort/GamiPort/GamiPort.csproj

# Build entire solution
dotnet build GamiPort/GamiPort.sln
```

### Run
```bash
# Run GameSpace (Admin)
cd GameSpace/GameSpace
dotnet run

# Run GamiPort (Public)
cd GamiPort/GamiPort
dotnet run
```

### Database Operations
```bash
# DO NOT use migrations - database is pre-existing
# To verify connection:
# Visit /healthz/db (GameSpace only) - should return {"status":"ok"}

# View database via SSMS:
# Server: DESKTOP-8HQIS1S\SQLEXPRESS (or similar local instance)
# Database: GameSpacedatabase
```

### Testing
No automated test projects currently exist. Manual testing via browser required.

## Area-Based Development Rules

### Critical Constraints
1. **Zero Cross-Boundary Modification**: When working in an Area (e.g., `Areas/MiniGame/`), you may ONLY modify files within that Area directory
2. **Program.cs Exception**: Only add minimal required registrations for your Area; do not modify other Area configurations
3. **Shared Resources**: Do NOT modify:
   - `wwwroot/lib/sb-admin/` (GameSpace)
   - `wwwroot/lib/bootstrap/`
   - `wwwroot/lib/font-awesome/`
   - Shared layouts in `Views/Shared/`

### MiniGame Area Specifics
- **Backend (GameSpace)**: `Areas/MiniGame/**` - Admin controllers, services, views (COMPLETED)
- **Frontend (GamiPort)**: `Areas/MiniGame/**` - Client-facing features (IN PROGRESS)
- **Allowed Controllers**: Pattern `Admin*Controller` for backend
- **Sidebar Navigation**: Two-level hierarchy via `_Sidebar.cshtml`

### Recommended Area Structure
```
Areas/YourArea/
├── Controllers/
├── ApiControllers/        # RESTful endpoints (GamiPort pattern)
├── Services/              # Business logic layer
├── Models/                # ViewModels, DTOs
├── Views/
├── wwwroot/               # Area-specific static files
│   ├── js/
│   ├── css/
│   └── unity/             # Unity WebGL builds (MiniGame only)
├── Filters/               # Custom attributes
├── Helpers/               # Utility classes
└── Constants/             # Constant definitions
```

## SignalR Hubs

### GameSpace
- **ChatHub**: `/hubs/chat` (DM functionality)
- **SupportHub**: `/hubs/support` (customer support)

### GamiPort
- **ChatHub**: `/hubs/chat` (DM functionality)
- **SupportHub**: `/hubs/support` (customer support - single endpoint shared with admin)
- **HttpTransportType**: Configured for WebSockets, ServerSentEvents, LongPolling

## MiniGame Area Business Logic

### Admin Functions (GameSpace - COMPLETED)
1. **Wallet Management**:
   - Query user points, coupons, e-vouchers
   - Issue points, coupons, e-vouchers
   - View transaction history (`WalletHistory`)

2. **Sign-in System**:
   - Configure sign-in rules (`SignInRule`)
   - View user sign-in records (`UserSignInStats`)

3. **Pet System**:
   - Configure global rules (level-up, interaction bonuses, skin/background costs)
   - Manually adjust individual pet data
   - Query pet list with change history
   - Pet attributes: Hunger/Mood/Stamina/Cleanliness/Health (0-100 range)
   - Skin color: `varchar(7)` format `#RRGGBB`

4. **MiniGame System**:
   - Configure reward rules and daily play limits (default: 3/day via `SystemSettings`)
   - View game records (`MiniGame` table: `startTime`, `endTime`, `result`, rewards)

### Client Functions (GamiPort - IN PROGRESS)
1. **Wallet**: View points, redeem coupons/e-vouchers, view transaction history
2. **Sign-in**: Calendar view, perform daily sign-in, view history
3. **Pet**: Name change, interactions (feed/bathe/play/sleep), skin/background change (costs points)
4. **MiniGame**: Start adventure (returns `sessionId`, remaining plays), view game records

### Frontend Technology Stack (GamiPort MiniGame)
- **Vue.js 3**: Via CDN, components in `Areas/MiniGame/wwwroot/js/vue-components/`
- **Unity WebGL**: Builds in `Areas/MiniGame/wwwroot/unity/{PetInteraction,PetAdventure}/Build/`
- **Progressive Enhancement**: Razor Views provide initial HTML, Vue enhances interactivity
- **Zero Cross-Boundary**: All frontend assets must stay within `Areas/MiniGame/wwwroot/`

## Common Patterns

### Service Registration (Program.cs)
```csharp
// MiniGame Area example
builder.Services.AddMiniGameServices(builder.Configuration);

// social_hub services
builder.Services.AddScoped<IMuteFilter, MuteFilter>();
builder.Services.AddScoped<INotificationService, NotificationService>();
builder.Services.AddSingleton<ISupportNotifier, BackendSignalRSupportNotifier>();
```

### Repository Pattern
Services typically inject `GameSpacedatabaseContext` directly (no separate repository layer). Use `AsNoTracking()` for read-only queries.

### Transaction Management
```csharp
using var transaction = await _context.Database.BeginTransactionAsync();
try {
    // Wallet deduction, reward granting, etc.
    await _context.SaveChangesAsync();
    await transaction.CommitAsync();
}
catch {
    await transaction.RollbackAsync();
    throw;
}
```

### Idempotency
Batch operations limit: ≤ 1000 records. Write operations should be idempotent where possible.

### Error Handling
- Use `ProblemDetails` for API errors
- Custom filter: `MiniGameProblemDetailsFilter` (GameSpace MiniGame Area)
- Logging: Serilog + CorrelationId for audit trails

### Encoding
**All files must be UTF-8 with BOM** (especially for Chinese content).

## Configuration Management

### SystemSettings Table (Dynamic Configuration)
- 36 business rules configurable via admin UI
- 30-minute cache (no restart required)
- Fields: `SettingKey`, `SettingValue`, `Category`, `SettingType` (String/Boolean/Number/JSON), `IsReadOnly`, `IsActive`
- Audit fields: `UpdatedBy`, `UpdatedAt`

Example keys:
- `MiniGame.DailyPlayLimit` → Default: 3
- `Pet.InteractionCooldown` → Seconds between interactions
- `SignIn.ConsecutiveDayBonus` → Bonus multiplier

## Important Architectural Decisions

1. **No EF Migrations**: Database is pre-created and seeded via SSMS scripts
2. **Area Isolation**: Each Area operates independently; shared code goes in `Infrastructure/`
3. **No Global SPA**: Each page is server-rendered Razor; Vue/React used for progressive enhancement only
4. **Dual Authentication**: Admin uses `AdminCookie`, public uses `GamiPort.User` - they do not interfere
5. **SignalR Cross-Origin**: GamiPort acts as SignalR host for both frontend and backend clients
6. **Time Zone**: Standardized on `TimeZones.Taipei` via `IAppClock` / `AppClock`

## Code Quality Standards

1. **File Size**: Commits ≤ 3 files or ≤ 400 lines per commit (CI enforcement)
2. **Constraints**: All DB constraints (PK/FK/UNIQUE/CHECK/DEFAULT) must be honored
3. **Soft Delete**: Many tables use `IsDeleted`, `DeletedAt`, `DeletedBy`, `DeleteReason` pattern
4. **Response Caching**: Disabled globally via `ResponseCacheAttribute` to prevent stale HTML after login

## Troubleshooting

### Common Issues

**Connection String Not Found**
- Check `appsettings.json` → `ConnectionStrings` section
- GameSpace looks for: `DefaultConnection`, then `GameSpace`/`GameSpacedatabase`
- GamiPort looks for: `GameSpace`, then `GameSpacedatabase`, then `DefaultConnection`

**401 Unauthorized in Admin**
- Verify `AdminCookie` is set and contains `IsManager=true` claim
- Check `ManagerData` table for user record
- Verify `ManagerRolePermission` grants required permissions

**SignalR Connection Failed**
- Verify CORS policy includes correct origin (GameSpace ports: 7042/5211)
- Check if hub route is mapped in `Program.cs` → `app.MapHub<T>(path)`
- Ensure `AllowCredentials()` is set in CORS policy

**404 Not Found**
- Shared 404 page exists at application level (DO NOT create Area-specific 404 pages)
- Check Area routing: `{area:exists}/{controller=Home}/{action=Index}/{id?}`

**Chinese Characters Display as ???**
- Ensure file is saved as UTF-8 with BOM
- Check `appsettings.json` does not override encoding

## Reference Documentation

See `schema/` directory for detailed specifications:
- `README_合併版.md` - Complete project specification (Chinese)
- `MiniGame_Area_完整描述文件.md` - MiniGame Area detailed specs
- `完整資料庫架構文件.md` - Full database schema reference
- `前台開發藍圖文件.md` - Frontend development blueprint (Vue + Unity)
- `後台架構分析文件.md` - Backend architecture analysis
- `SQL_Server_連線操作完整手冊_AI適用.md` - SQL Server operations manual

## Git Workflow

**Current Branch**: `dev`
**Main Branch**: (Not specified - likely `main` or `master`)

When committing:
- Follow conventional commits format
- Include "why" not just "what" in messages
- Append footer:
  ```
  🤖 Generated with [Claude Code](https://claude.com/claude-code)

  Co-Authored-By: Claude <noreply@anthropic.com>
  ```
