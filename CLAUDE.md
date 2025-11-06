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
- **Server**: DESKTOP-8HQIS1S\SQLEXPRESS (or similar local instance)
- **Connection String**: Located in `appsettings.json` → `ConnectionStrings:GameSpace` (or `GameSpacedatabase` or `DefaultConnection`)
- **DbContext**: `GameSpacedatabaseContext` (in `Models/` for both projects)
- **Total Tables**: 103 tables across all areas
- **Schema Files**: Reference files in `schema/` directory (for AI reference only)
- **Database Priority**: When implementing features, ALWAYS:
  1. Connect to actual SQL Server database to verify schema
  2. Check seed data for actual values and constraints
  3. Verify field types, lengths, nullability, FK/PK/UK/CHECK/Identity
  4. Align 100% with database structure (no assumptions)

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

### Critical Constraints (STRICT ENFORCEMENT)

1. **Zero Cross-Boundary Modification**: When working in an Area (e.g., `Areas/MiniGame/`), you may ONLY modify files within that Area directory
   - **For GamiPort MiniGame work**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame`
   - **All documentation** (RUNLOG.md, HANDOFF.md, CHECKLIST.md) must be placed within the Area boundary
   - **PAUSE-AND-ASK Mode**: If you determine cross-boundary modification is necessary:
     - **STOP** all modifications immediately
     - **Report**:
       1. Current situation and why changes cannot be completed within Area
       2. Solution alternatives with pros/cons for each approach
       3. Exact file paths requiring modification (outside Area boundary)
       4. **Unified diff blocks** showing: original code → proposed code for EACH file
     - **DO NOT PROCEED** until explicit user approval is granted
     - This applies even to seemingly minor changes (Program.cs, shared layouts, Infrastructure/, etc.)

2. **Program.cs Exception**: Only add minimal required registrations for your Area; do not modify other Area configurations without PAUSE-AND-ASK

3. **Shared Resources - DO NOT MODIFY**:
   - `wwwroot/lib/sb-admin/` (GameSpace)
   - `wwwroot/lib/bootstrap/`
   - `wwwroot/lib/font-awesome/`
   - `Views/Shared/` layouts
   - `Infrastructure/` utilities (unless adding new Area-specific files)
   - Any files in other Areas (Forum, OnlineStore, social_hub, etc.)

### MiniGame Area Specifics
- **Backend (GameSpace)**: `Areas/MiniGame/**` - Admin controllers, services, views (COMPLETED)
  - 24 controllers, 94 services fully implemented
  - Reference backend code for business logic patterns
- **Frontend (GamiPort)**: `Areas/MiniGame/**` - Client-facing features (IN PROGRESS)
  - 14 functions required (13 core + 1 bonus: sign-in rule preview)
  - Pet interaction page with "Start Adventure" button in bottom-right
  - Adventure game inspired by Chrome dinosaur runner
- **Allowed Controllers**: Pattern `Admin*Controller` for backend
- **Sidebar Navigation**: Two-level hierarchy via `_Sidebar.cshtml`
- **Static Assets**: Must be placed in `Areas/MiniGame/wwwroot/`
  - Images: `PetBackgroundCostSettings表格_種子資料_圖片/`
  - JavaScript: `js/` (including `pet-avatar.js`)
  - Unity builds: `unity/{PetInteraction,PetAdventure}/Build/`

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
  - Pet Adventure game inspired by Chrome dinosaur runner game
  - WebGL output must be placed in Area-specific wwwroot
- **Pet Avatar SVG Renderer**: `pet-avatar.js` for dynamic pet visualization
- **Progressive Enhancement**: Razor Views provide initial HTML, Vue/JS enhances interactivity
- **Zero Cross-Boundary**: All frontend assets must stay within `Areas/MiniGame/wwwroot/`
- **Anti-Forgery Tokens**: Always include `@Html.AntiForgeryToken()` in forms and AJAX POST requests

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

### Time Zone Handling (CRITICAL)
**All time operations MUST use `IAppClock` for UTC+8 Taiwan timezone:**

```csharp
// ❌ WRONG - Never use these directly
var now = DateTime.Now;
var utcNow = DateTime.UtcNow;

// ✅ CORRECT - Always use IAppClock
private readonly IAppClock _appClock;
var appNow = _appClock.ToAppTime(_appClock.UtcNow);  // UTC+8 Taiwan time
```

**In Razor Views:**
```csharp
@inject GamiPort.Infrastructure.Time.IAppClock AppClock
@{
    var today = AppClock.ToAppTime(AppClock.UtcNow);
    var currentYear = today.Year;
}
```

**Recent Fix**: SignInService consecutive days calculation bug (showed 9 days when only signed in 1 day) was caused by incorrect date logic. Always calculate from `today` going backwards, breaking on first gap.

### Code Generation Best Practices

1. **Unique Code Generation** (Coupons/Vouchers):
   - ❌ BAD: `new Random().Next(100000, 999999)` - High collision risk
   - ✅ GOOD: GUID-based with retry mechanism and UTC+8 timestamp
   ```csharp
   private async Task<string> GenerateUniqueCodeAsync()
   {
       int maxRetries = 10;
       for (int i = 0; i < maxRetries; i++)
       {
           var appNow = _appClock.ToAppTime(_appClock.UtcNow);  // Use UTC+8
           var code = $"PREFIX-{appNow:yyyyMM}-{Guid.NewGuid():N}"[..30];
           if (!await _context.Codes.AnyAsync(c => c.Code == code))
               return code;
           _logger.LogWarning("Code collision, retrying: {Code}, Attempt={Attempt}", code, i + 1);
       }
       throw new Exception("Failed to generate unique code after retries");
   }
   ```

2. **AJAX Response Handling & Real-time UI Updates**:
   - Always validate complete data structures before updating UI
   - Update all related UI elements (progress bars, badges, counters)
   - Avoid unreliable CSS selectors (`:has()`, `:contains()`)
   ```javascript
   // ✅ GOOD - Direct ID-based updates
   function updatePetStats(pet) {
       if (typeof pet.hunger === 'number') {
           const bar = document.getElementById('hunger-bar');
           bar.style.width = pet.hunger + '%';
       }

       // Update experience bar with proper proportion
       if (typeof pet.experience === 'number' && typeof pet.experienceToNextLevel === 'number') {
           updateExperienceBar(pet.experience, pet.experienceToNextLevel);
       }

       // Fallback if incomplete
       if (!pet.hunger || !pet.experience) {
           console.log('Pet data incomplete, reloading...');
           setTimeout(() => window.location.reload(), 1000);
       }
   }
   ```

3. **Image Paths & Background Images**:
   - Always use absolute paths from Area root: `/MiniGame/subfolder/image.png`
   - Background images correct path: `/MiniGame/PetBackgroundCostSettings表格_種子資料_圖片/`
   - Verify image preloading with error handlers:
   ```javascript
   const img = new Image();
   img.onload = () => console.log('Loaded:', path);
   img.onerror = () => {
       console.error('Failed:', path);
       element.style.backgroundImage = 'linear-gradient(...)'; // Fallback
   };
   img.src = path;
   ```

4. **Anti-Forgery Protection**:
   - Include token in forms: `@Html.AntiForgeryToken()`
   - Pass in AJAX: `__RequestVerificationToken=${encodeURIComponent(token)}`

5. **CSS Z-Index Layer Management**:
   - Global UI elements: 1080-1090 (QuickFab, FriendDock, FloatingDock)
   - Area-specific critical buttons (e.g., "出發冒險"): 1100+
   - Always verify z-index hierarchy to avoid hidden elements

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

## UI/UX Standards (GamiPort MiniGame)

### Design System
- **Overall Style**: Bahamut-inspired layout structure
- **MiniGame Color Scheme**: Light blue modern palette (淡藍現代系配色)
- **Primary Color**: `#17a2b8` (teal/cyan) for main actions
- **Neutral Backgrounds**: `#f0f4f8`, `#f9f9f9` for cards and sections
- **Border Radius**: 8px-24px for modern rounded corners
- **Shadows**: Subtle `0 2px 8px rgba(0,0,0,0.1)` for depth

### Component Consistency
- **Buttons**: Clear hover/active states, consistent padding (8px-16px)
- **Cards**: White background, rounded corners, subtle shadows
- **Forms**: Bootstrap-based with custom styling, clear validation feedback
- **Loading States**: Always show loading indicators for async operations
- **Error Messages**: User-friendly Chinese messages with context

### Accessibility & Responsiveness
- Keyboard navigation support where applicable
- Chinese text readability (UTF-8 with BOM)
- Responsive design (mobile-friendly layouts)
- Clear visual feedback for all interactions

## Code Quality Standards (STRICT ENFORCEMENT)

1. **Zero Compilation Errors**:
   - Every commit MUST build successfully: `dotnet build` → 0 errors
   - Warnings are acceptable; errors are not
   - Verify build before git commit

2. **Database Constraint Compliance**:
   - All DB constraints must be honored: PK/FK/UNIQUE/CHECK/DEFAULT/Identity
   - Field lengths, types, nullability must match exactly
   - Soft delete pattern: `IsDeleted`, `DeletedAt`, `DeletedBy`, `DeleteReason`

3. **No Placeholder Code**:
   - Never use TODO, "略", "待實現", or incomplete implementations
   - All code must be production-ready
   - If functionality cannot be completed, use PAUSE-AND-ASK mode

4. **File Encoding**:
   - All files MUST be UTF-8 with BOM (especially Chinese content)
   - Verify encoding if Chinese characters display as ???

5. **Boundary Compliance**:
   - All modifications must stay within `GamiPort/GamiPort/Areas/MiniGame/`
   - Documentation files must also be within Area boundary
   - Cross-boundary changes require PAUSE-AND-ASK approval

6. **Time Zone Consistency**:
   - Use `IAppClock.ToAppTime(_appClock.UtcNow)` for all time operations
   - Never use `DateTime.Now` or `DateTime.UtcNow` directly
   - All times must be UTC+8 Taiwan timezone

7. **Response Caching**:
   - Disabled globally via `ResponseCacheAttribute` to prevent stale HTML after login

8. **File Size** (suggested):
   - Commits ≤ 3 files or ≤ 400 lines per commit for reviewability
   - Break large changes into logical chunks

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

## Development Workflow

### Documentation Requirements (MANDATORY)
When working on MiniGame Area features, maintain these files **within Area boundary** at `GamiPort/GamiPort/Areas/MiniGame/`:

- **RUNLOG.md**: Chronological log (Taipei timezone) of "what was done, why, next steps"
  - Record technical decisions and rationale
  - Note file modifications with line numbers
  - Include git commit hashes for major milestones

- **HANDOFF.md**: Handoff document for continuation with TO-DO list
  - Current state summary
  - Completed tasks (with checkmarks)
  - Pending tasks prioritized (P0/P1/P2)
  - Known issues and blockers

- **CHECKLIST.md**: Checkbox-style verification list
  - Database table alignment (16 core tables)
  - Function implementation status (14 required functions)
  - Bug fixes status
  - Code quality checks (build errors, timezone, boundaries)
  - Business rules validation

**Update Timing**:
- Start of session: Read all three files to understand continuation point
- During work: Update as tasks complete (real-time tracking)
- End of session: Final update for next session's "zero-guessing" continuation

### Development Sequence (MiniGame Area)
1. **Database Verification FIRST**:
   - Connect to actual SQL Server database
   - Verify schema, seed data, constraints (PK/FK/UK/CHECK/Identity)
   - Document actual field types, lengths, nullability
   - Note: Schema files are reference only; DB is source of truth

2. **Views Second**:
   - Start with Razor views, UI/UX implementation
   - Follow Bahamut-inspired layout with light blue modern color scheme
   - Ensure responsive design and Chinese text readability

3. **Models Third**:
   - Create ViewModels/DTOs 100% aligned with verified DB schema
   - Reference backend (GameSpace MiniGame) for naming patterns

4. **Controllers/Services Fourth**:
   - Implement business logic matching backend patterns
   - Use `IAppClock` for all time operations
   - Implement proper transaction management and error handling

5. **Testing**:
   - Manual browser testing (no automated tests)
   - Verify all AJAX interactions update UI in real-time
   - Test timezone consistency (UTC+8)

6. **Git Backup**:
   - Commit after each small milestone
   - Build must pass with 0 errors
   - Use dev branch only (no new branches)

### Reading Hierarchy (When Implementing Features)
**CRITICAL**: When conflicts arise, follow this strict priority order:

1. **SQL Server Database** (actual schema and seed data) - **CONNECT AND VERIFY**
   - Field types, lengths, nullability, constraints
   - Seed data for actual values and patterns
   - Foreign keys, primary keys, unique keys, CHECK constraints, Identity columns

2. **Backend Architecture** (GameSpace MiniGame Area existing code)
   - 24 controllers, 94 services fully implemented
   - Business logic patterns, naming conventions
   - Service layer architecture and transaction management

3. **schema/README_合併版.md** - Section 3: Frontend Requirements (14 functions)
   - 3.1 會員錢包 (6 functions)
   - 3.2 會員簽到系統 (2 + 1 bonus functions)
   - 3.3 寵物系統 (4 functions)
   - 3.4 小遊戲系統 (2 functions)

4. **schema/前台開發藍圖文件.md** - Frontend implementation blueprint

5. **Other schema documentation** (reference materials only)

**Important**: If documentation conflicts with actual database, **database wins**. Always verify assumptions by connecting to SQL Server.

### Progress Tracking
- Start each session by reading RUNLOG.md/HANDOFF.md to continue from last checkpoint
- Update all three documentation files before ending work session
- Ensure "zero-guessing" continuation for next session

## Git Workflow

**Current Branch**: `dev` (DO NOT create new branches)
**Main Branch**: (Not specified - likely `main` or `master`)

### Commit Strategy
- Commit frequently after completing small milestones
- Build must pass with 0 errors before committing
- Include timestamp and milestone description in commit message

### Commit Message Format
```
feat/fix(Area Name): Brief description in Chinese

## Detailed changes (if needed)
- Change 1
- Change 2

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Examples:**
```
feat(GamiPort MiniGame): 實作簽到規則預覽功能
fix(GamiPort MiniGame): 修復優惠券兌換失敗問題
fix(GamiPort MiniGame): 修復寵物系統、簽到算法及全局時區問題
refactor(MiniGame): 移動文檔至正確邊界內
```

## Multi-Agent Workflow (RECOMMENDED)

When working on complex tasks, use parallel agents for maximum efficiency:

### Agent Usage Patterns
```
User Request: "Fix multiple UI bugs across different pages"
→ Launch 4 parallel agents:
  - Agent 1 (Sonnet): Pet/Index.cshtml fixes
  - Agent 2 (Sonnet): Pet/Customize.cshtml optimizations
  - Agent 3 (Sonnet): Service layer algorithm fixes
  - Agent 4 (Haiku): View timezone corrections
```

### Agent Best Practices
1. **Use parallel agents** for independent tasks (UI fixes, different pages, separate services)
2. **Provide complete context** to each agent (file paths, specific issues, expected solutions)
3. **Specify model tier**: Haiku for simple tasks, Sonnet for complex logic, Opus for architecture
4. **Aggregate results**: Collect all agent outputs, verify consistency, commit together
5. **Diagnostic before implementation**: Use agents to analyze root causes before coding

### Recent Success Example
**Task**: Fix 12 bugs across Pet system, Sign-in, Wallet, and global timezone
**Approach**: 4 parallel diagnostic agents → identified root causes → 4 parallel implementation agents
**Result**: All fixes completed in single session, 0 errors, pushed to dev branch
