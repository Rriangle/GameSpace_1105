# Pet Customize Feature - Complete Fix Solution

## Problem Diagnosis

### ROOT CAUSE
The database does NOT have a dedicated purchase tracking table for pet skins and backgrounds. The current `UpdatePetAppearanceAsync` method treats every appearance change as both a **purchase AND application** in one step, without recording ownership history.

### Issues Identified

1. **0-point items cannot be applied**
   - Problem: The logic only updates when `pet.SkinColor != skinColor`
   - Since there's no purchase tracking, a 0-point item is "purchased" but never recorded
   - When you try to apply it again, the system thinks it's a new purchase attempt

2. **No purchase status tracking**
   - Without a purchase tracking table, the system cannot distinguish between:
     - "Owned but not applied"
     - "Not owned at all"

3. **Repeated purchases possible**
   - Nothing prevents buying the same item multiple times
   - Wastes user points

4. **Background preview not working**
   - Frontend code exists but has event binding issues

## Solution Strategy

Since **database schema modifications are STRICTLY PROHIBITED**, we use a smart workaround:

### Purchase Tracking via WalletHistory
- Use existing `WalletHistory` table with ItemCode pattern:
  - `PET_SKIN_{ColorCode}` - for skin color purchases
  - `PET_BG_{BackgroundCode}` - for background purchases
- Query this table to determine what user has purchased

### Free Items Logic
- 0-point items are considered "always owned"
- Current applied skin/background is considered "owned"

### Separation of Concerns
- **Purchase**: Buy an item (deduct points, record in WalletHistory)
- **Apply**: Switch to an owned item (free, just update Pet table)

## Implementation

### 1. Service Interface Updates

**File**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame\Services\IPetService.cs`

Add these method signatures (已完成):

```csharp
/// <summary>
/// 獲取用戶已購買的膚色列表
/// </summary>
Task<IEnumerable<string>> GetPurchasedSkinColorsAsync(int userId);

/// <summary>
/// 獲取用戶已購買的背景列表
/// </summary>
Task<IEnumerable<string>> GetPurchasedBackgroundsAsync(int userId);

/// <summary>
/// 購買膚色（不套用）
/// </summary>
Task<PetPurchaseResult> PurchaseSkinColorAsync(int userId, string skinColor);

/// <summary>
/// 購買背景（不套用）
/// </summary>
Task<PetPurchaseResult> PurchaseBackgroundAsync(int userId, string background);

/// <summary>
/// 套用已購買的膚色
/// </summary>
Task<PetApplyResult> ApplySkinColorAsync(int userId, string skinColor);

/// <summary>
/// 套用已購買的背景
/// </summary>
Task<PetApplyResult> ApplyBackgroundAsync(int userId, string background);
```

Add these result classes (已完成):

```csharp
public class PetPurchaseResult
{
    public bool Success { get; set; }
    public string Message { get; set; } = string.Empty;
    public int PointsSpent { get; set; }
    public int RemainingPoints { get; set; }
}

public class PetApplyResult
{
    public bool Success { get; set; }
    public string Message { get; set; } = string.Empty;
    public Pet? Pet { get; set; }
}
```

### 2. Service Implementation

**File**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame\Services\PetService.cs`

The implementation code is in: `PetService_NewMethods.cs`

**Manual Action Required**: Copy all methods from `PetService_NewMethods.cs` and paste them into `PetService.cs` BEFORE the last closing `}` of the class.

Key methods:
- `GetPurchasedSkinColorsAsync` - Tracks ownership via WalletHistory
- `GetPurchasedBackgroundsAsync` - Tracks ownership via WalletHistory
- `PurchaseSkinColorAsync` - Purchase logic with duplicate check
- `PurchaseBackgroundAsync` - Purchase logic with duplicate check
- `ApplySkinColorAsync` - Apply owned skin
- `ApplyBackgroundAsync` - Apply owned background

### 3. Controller Updates

**File**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame\Controllers\PetController.cs`

Add these new action methods:

```csharp
/// <summary>
/// GET: 獲取已購買項目狀態
/// </summary>
[HttpGet]
public async Task<IActionResult> GetPurchaseStatus()
{
	if (User.Identity?.IsAuthenticated != true)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var userId = _appCurrentUser.UserId;
	if (userId <= 0)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var purchasedSkins = await _petService.GetPurchasedSkinColorsAsync(userId);
	var purchasedBackgrounds = await _petService.GetPurchasedBackgroundsAsync(userId);

	return Json(new
	{
		success = true,
		purchasedSkins = purchasedSkins,
		purchasedBackgrounds = purchasedBackgrounds
	});
}

/// <summary>
/// POST: 購買膚色
/// </summary>
[HttpPost]
public async Task<IActionResult> PurchaseSkinColor(string skinColor)
{
	if (User.Identity?.IsAuthenticated != true)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var userId = _appCurrentUser.UserId;
	if (userId <= 0)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var result = await _petService.PurchaseSkinColorAsync(userId, skinColor);

	return Json(new
	{
		success = result.Success,
		message = result.Message,
		pointsSpent = result.PointsSpent,
		remainingPoints = result.RemainingPoints
	});
}

/// <summary>
/// POST: 購買背景
/// </summary>
[HttpPost]
public async Task<IActionResult> PurchaseBackground(string background)
{
	if (User.Identity?.IsAuthenticated != true)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var userId = _appCurrentUser.UserId;
	if (userId <= 0)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var result = await _petService.PurchaseBackgroundAsync(userId, background);

	return Json(new
	{
		success = result.Success,
		message = result.Message,
		pointsSpent = result.PointsSpent,
		remainingPoints = result.RemainingPoints
	});
}

/// <summary>
/// POST: 套用膚色
/// </summary>
[HttpPost]
public async Task<IActionResult> ApplySkinColor(string skinColor)
{
	if (User.Identity?.IsAuthenticated != true)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var userId = _appCurrentUser.UserId;
	if (userId <= 0)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var result = await _petService.ApplySkinColorAsync(userId, skinColor);

	return Json(new
	{
		success = result.Success,
		message = result.Message,
		pet = result.Pet != null ? new
		{
			skinColor = result.Pet.SkinColor,
			skinColorChangedTime = result.Pet.SkinColorChangedTime.ToString("yyyy-MM-dd HH:mm:ss")
		} : null
	});
}

/// <summary>
/// POST: 套用背景
/// </summary>
[HttpPost]
public async Task<IActionResult> ApplyBackground(string background)
{
	if (User.Identity?.IsAuthenticated != true)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var userId = _appCurrentUser.UserId;
	if (userId <= 0)
	{
		return Json(new { success = false, message = "請先登入" });
	}

	var result = await _petService.ApplyBackgroundAsync(userId, background);

	return Json(new
	{
		success = result.Success,
		message = result.Message,
		pet = result.Pet != null ? new
		{
			backgroundColor = result.Pet.BackgroundColor,
			backgroundColorChangedTime = result.Pet.BackgroundColorChangedTime.ToString("yyyy-MM-dd HH:mm:ss")
		} : null
	});
}
```

### 4. Frontend Customize.cshtml Updates

**File**: `C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort\Areas\MiniGame\Views\Pet\Customize.cshtml`

#### JavaScript State Management

Add these global variables at the top of the script section:

```javascript
// Purchase status tracking
let purchasedSkins = [];
let purchasedBackgrounds = [];
let originalSkinColor = '@currentSkinColor';
let originalBackgroundColor = '@currentBackgroundColor';
```

#### Load Purchase Status on Page Load

Replace the DOMContentLoaded event with:

```javascript
document.addEventListener('DOMContentLoaded', async function () {
    // Initialize Pet Avatar for Preview
    const petData = {
        hunger: @(Model?.Hunger ?? 50),
        mood: @(Model?.Mood ?? 50),
        stamina: @(Model?.Stamina ?? 50),
        cleanliness: @(Model?.Cleanliness ?? 50),
        health: @(Model?.Health ?? 50),
        skinColor: '@currentSkinColor',
        level: @(Model?.Level ?? 1)
    };

    previewPetAvatar = new PetAvatar('customizePetAvatarContainer', petData);

    // Load purchase status
    await loadPurchaseStatus();

    // Initialize grids with purchase status
    initializeSkinColors();
    initializeBackgroundColors();
});

async function loadPurchaseStatus() {
    try {
        const response = await fetch('/MiniGame/Pet/GetPurchaseStatus');
        const result = await response.json();

        if (result.success) {
            purchasedSkins = result.purchasedSkins || [];
            purchasedBackgrounds = result.purchasedBackgrounds || [];
            console.log('[Purchase Status] Skins:', purchasedSkins, 'Backgrounds:', purchasedBackgrounds);
        }
    } catch (error) {
        console.error('[Purchase Status] Failed to load:', error);
    }
}
```

#### Update initializeSkinColors Function

```javascript
function initializeSkinColors() {
    const grid = document.getElementById('skinColorGrid');
    grid.innerHTML = '';
    skinColorOptions.forEach(option => {
        const div = document.createElement('div');
        const isSelected = option.color === selectedSkinColor;
        const isDisabled = option.isExpired;
        const isPurchased = purchasedSkins.includes(option.color);

        div.className = `color-option ${isSelected ? 'selected' : ''} ${isDisabled ? 'disabled' : ''}`;

        if (!isDisabled) {
            div.onclick = () => selectSkinColor(option.color, option.cost, isPurchased);
        }

        let badge = '';
        if (isPurchased && !isDisabled) {
            badge = '<span class="badge bg-success" style="font-size: 0.65rem; position: absolute; top: -8px; right: -8px;">已購買</span>';
        }

        div.innerHTML = `
            <div style="position: relative;">
                <div class="color-swatch" style="background-color: ${option.color}; ${isDisabled ? 'opacity: 0.4; cursor: not-allowed;' : ''}"></div>
                ${badge}
            </div>
            <div class="color-label" style="${isDisabled ? 'color: #999;' : ''}">${option.name}</div>
            <div class="color-cost" style="${isDisabled ? 'background: #e0e0e0; color: #999;' : ''}">${option.cost} 點</div>
        `;
        grid.appendChild(div);
    });
}
```

#### Update initializeBackgroundColors Function

```javascript
function initializeBackgroundColors() {
    const grid = document.getElementById('backgroundColorGrid');
    grid.innerHTML = '';
    backgroundColorOptions.forEach(option => {
        const div = document.createElement('div');
        const isSelected = option.code === selectedBackgroundColor;
        const isDisabled = option.isExpired;
        const isPurchased = purchasedBackgrounds.includes(option.code);

        div.className = `background-option ${isSelected ? 'selected' : ''} ${isDisabled ? 'disabled' : ''}`;

        let badge = '';
        if (isPurchased && !isDisabled) {
            badge = '<span class="badge bg-success" style="font-size: 0.65rem; position: absolute; top: -8px; right: -8px;">已購買</span>';
        }

        div.innerHTML = `
            <div style="position: relative;">
                <div class="background-swatch" style="background-image: url('${option.image}'); background-size: cover; background-position: center; ${isDisabled ? 'opacity: 0.4; cursor: not-allowed;' : ''}"></div>
                ${badge}
            </div>
            <div class="color-label" style="${isDisabled ? 'color: #999;' : ''}">${option.name}</div>
            <div class="color-cost" style="${isDisabled ? 'background: #e0e0e0; color: #999;' : ''}">${option.cost} 點</div>
        `;

        if (!isDisabled) {
            (function(opt, element, purchased) {
                element.addEventListener('click', function(event) {
                    selectBackgroundColor(opt.code, opt.cost, opt.image, element, purchased);
                    event.preventDefault();
                    event.stopPropagation();
                });
            })(option, div, isPurchased);
        } else {
            div.style.cursor = 'not-allowed';
            div.style.pointerEvents = 'none';
            div.style.opacity = '0.6';
        }

        grid.appendChild(div);
    });
}
```

#### Update selectSkinColor Function

```javascript
function selectSkinColor(color, cost, isPurchased) {
    selectedSkinColor = color;
    document.querySelectorAll('.color-option').forEach(el => el.classList.remove('selected'));
    event.target.closest('.color-option').classList.add('selected');
    document.getElementById('skinColorCost').textContent = isPurchased ? '0（已購買）' : cost;

    // Update preview
    if (previewPetAvatar) {
        previewPetAvatar.updateSkinColor(color);
    }

    // Update button text
    const confirmBtn = document.getElementById('confirmSkinColor');
    confirmBtn.disabled = false;
    confirmBtn.innerHTML = isPurchased
        ? '<i class="bi bi-check-lg me-2"></i>套用膚色'
        : '<i class="bi bi-cart-plus me-2"></i>確認購買';
}
```

#### Update selectBackgroundColor Function

```javascript
function selectBackgroundColor(code, cost, image, clickedElement, isPurchased) {
    selectedBackgroundColor = code;
    selectedBackgroundImage = image;

    // Update selection
    document.querySelectorAll('.background-option').forEach(el => el.classList.remove('selected'));
    if (clickedElement) {
        clickedElement.classList.add('selected');
    }

    // Update cost
    document.getElementById('backgroundColorCost').textContent = isPurchased ? '0（已購買）' : cost;

    // Update preview
    const previewCard = document.getElementById('previewCard');
    let imagePath = image;
    if (!imagePath.startsWith('/')) {
        imagePath = '/' + imagePath;
    }

    console.log('[Background Preview] Selected:', code, 'Cost:', cost, 'Purchased:', isPurchased, 'Image:', imagePath);

    previewCard.style.backgroundImage = 'none';
    previewCard.style.backgroundImage = `url('${imagePath}')`;
    previewCard.style.backgroundSize = 'cover';
    previewCard.style.backgroundPosition = 'center';
    previewCard.style.backgroundRepeat = 'no-repeat';
    previewCard.style.backgroundAttachment = 'scroll';
    previewCard.style.backgroundColor = 'transparent';

    void previewCard.offsetHeight;

    const img = new Image();
    img.onload = function() {
        console.log('[Background Preview] Image loaded successfully:', imagePath);
        if (selectedBackgroundColor === code) {
            previewCard.style.backgroundImage = `url('${imagePath}')`;
        }
    };
    img.onerror = function() {
        console.error('[Background Preview] Failed to load image:', imagePath);
        if (selectedBackgroundColor === code) {
            const fallbackGradient = 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
            previewCard.style.backgroundImage = fallbackGradient;
            console.warn('[Background Preview] Using fallback gradient instead');
        }
    };
    img.src = imagePath;

    // Update button text
    const confirmBtn = document.getElementById('confirmBackgroundColor');
    confirmBtn.disabled = false;
    confirmBtn.innerHTML = isPurchased
        ? '<i class="bi bi-check-lg me-2"></i>套用背景'
        : '<i class="bi bi-cart-plus me-2"></i>確認購買';
}
```

#### Update Confirm Button Handlers

```javascript
document.getElementById('confirmSkinColor').addEventListener('click', async function () {
    const selectedOption = skinColorOptions.find(o => o.color === selectedSkinColor);
    const cost = parseInt(selectedOption.cost);
    const isPurchased = purchasedSkins.includes(selectedSkinColor);

    if (isPurchased) {
        // Already purchased, just apply
        await applyCustomization('skin', selectedSkinColor, selectedOption.name);
    } else {
        // Need to purchase first
        await purchaseAndApply('skin', selectedSkinColor, selectedOption.name, cost);
    }
});

document.getElementById('confirmBackgroundColor').addEventListener('click', async function () {
    const selectedOption = backgroundColorOptions.find(o => o.code === selectedBackgroundColor);
    const cost = parseInt(selectedOption.cost);
    const isPurchased = purchasedBackgrounds.includes(selectedBackgroundColor);

    if (isPurchased) {
        // Already purchased, just apply
        await applyCustomization('background', selectedBackgroundColor, selectedOption.name);
    } else {
        // Need to purchase first
        await purchaseAndApply('background', selectedBackgroundColor, selectedOption.name, cost);
    }
});

async function purchaseAndApply(type, code, name, cost) {
    try {
        const token = document.querySelector('input[name="__RequestVerificationToken"]')?.value;

        // Step 1: Purchase
        const purchaseUrl = type === 'skin'
            ? '/MiniGame/Pet/PurchaseSkinColor'
            : '/MiniGame/Pet/PurchaseBackground';

        const purchaseParam = type === 'skin' ? 'skinColor' : 'background';

        const purchaseResponse = await fetch(purchaseUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'RequestVerificationToken': token || ''
            },
            body: `${purchaseParam}=${encodeURIComponent(code)}&__RequestVerificationToken=${encodeURIComponent(token || '')}`
        });

        const purchaseResult = await purchaseResponse.json();

        if (!purchaseResult.success) {
            alert(purchaseResult.message);
            return;
        }

        // Update points display
        document.getElementById('userPointsDisplay').textContent = purchaseResult.remainingPoints;

        // Update purchased list
        if (type === 'skin') {
            purchasedSkins.push(code);
        } else {
            purchasedBackgrounds.push(code);
        }

        // Step 2: Apply
        await applyCustomization(type, code, name);

        // Show purchase success message
        showSuccessMessage(purchaseResult.message);

        // Reload grids to show "已購買" badge
        if (type === 'skin') {
            initializeSkinColors();
        } else {
            initializeBackgroundColors();
        }
    } catch (error) {
        console.error('Purchase error:', error);
        alert('購買失敗，請重試');
    }
}

async function applyCustomization(type, code, name) {
    try {
        const token = document.querySelector('input[name="__RequestVerificationToken"]')?.value;

        const applyUrl = type === 'skin'
            ? '/MiniGame/Pet/ApplySkinColor'
            : '/MiniGame/Pet/ApplyBackground';

        const applyParam = type === 'skin' ? 'skinColor' : 'background';

        const applyResponse = await fetch(applyUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'RequestVerificationToken': token || ''
            },
            body: `${applyParam}=${encodeURIComponent(code)}&__RequestVerificationToken=${encodeURIComponent(token || '')}`
        });

        const applyResult = await applyResponse.json();

        if (applyResult.success) {
            // Update original values
            if (type === 'skin') {
                originalSkinColor = code;
            } else {
                originalBackgroundColor = code;
            }
            showSuccessMessage(`${type === 'skin' ? '膚色' : '背景'}套用成功`);
        } else {
            alert(applyResult.message);
        }
    } catch (error) {
        console.error('Apply error:', error);
        alert('套用失敗，請重試');
    }
}
```

#### Update Reset Functions

```javascript
function resetSkinColorSelection() {
    selectedSkinColor = originalSkinColor;
    initializeSkinColors();

    if (previewPetAvatar) {
        previewPetAvatar.updateSkinColor(selectedSkinColor);
    }

    document.getElementById('confirmSkinColor').disabled = true;
}

function resetBackgroundColorSelection() {
    selectedBackgroundColor = originalBackgroundColor;
    selectedBackgroundImage = '@($"/MiniGame/PetBackgroundCostSettings表格_種子資料_圖片/{currentBackgroundColor}.png")';

    initializeBackgroundColors();

    const previewCard = document.getElementById('previewCard');
    let imagePath = selectedBackgroundImage;
    if (!imagePath.startsWith('/')) {
        imagePath = '/' + imagePath;
    }

    console.log('[Background Reset] Restored to:', selectedBackgroundColor, 'Image:', imagePath);

    previewCard.style.backgroundImage = 'none';
    previewCard.style.backgroundImage = `url('${imagePath}')`;
    previewCard.style.backgroundSize = 'cover';
    previewCard.style.backgroundPosition = 'center';
    previewCard.style.backgroundRepeat = 'no-repeat';
    previewCard.style.backgroundAttachment = 'scroll';
    previewCard.style.backgroundColor = 'transparent';

    void previewCard.offsetHeight;

    document.getElementById('confirmBackgroundColor').disabled = true;
}
```

## Testing Checklist

### 1. Free Items (0 Points)
- [ ] Can click on 0-point skin color
- [ ] Button shows "套用膚色" (not "確認購買")
- [ ] Clicking button applies immediately without deducting points
- [ ] Returns to Pet page and skin is applied
- [ ] Repeat: Can click again and re-apply

### 2. Paid Items (Non-zero Points)
- [ ] Can click on paid skin color
- [ ] Button shows "確認購買"
- [ ] Clicking shows popup: "膚色：（名稱）購買成功，扣會員點數（X）點"
- [ ] Points deducted from wallet display
- [ ] Item now shows "已購買" badge
- [ ] Click again: button shows "套用膚色"
- [ ] Can apply for free

### 3. Already Purchased Items
- [ ] Shows "已購買" badge on grid
- [ ] Clicking shows button "套用"
- [ ] Clicking applies immediately (no purchase)
- [ ] Cost display shows "0（已購買）"

### 4. Cancel Button
- [ ] After purchase success, clicking Cancel returns to original appearance
- [ ] After applying purchased item, clicking Cancel KEEPS the applied appearance

### 5. Background Preview
- [ ] Clicking background immediately updates preview card background
- [ ] Background image displays correctly (not purple gradient)
- [ ] Background persists after purchase
- [ ] Background persists after apply

### 6. Insufficient Points
- [ ] Trying to purchase with insufficient points shows error
- [ ] Error message clearly states required vs available points
- [ ] No changes to wallet or purchase status

### 7. Duplicate Purchase Prevention
- [ ] Cannot purchase same item twice
- [ ] Error message: "此膚色已購買" / "此背景已購買"

## Files Modified/Created

1. **IPetService.cs** - Interface updated (completed)
2. **PetService.cs** - Implementation (needs manual copy from PetService_NewMethods.cs)
3. **PetController.cs** - New action methods (needs implementation)
4. **Customize.cshtml** - Frontend logic overhaul (needs implementation)

## Migration Notes

### WalletHistory ItemCode Patterns
- Skin purchases: `PET_SKIN_{ColorCode}` (e.g., `PET_SKIN_#FF5733`)
- Background purchases: `PET_BG_{BackgroundCode}` (e.g., `PET_BG_BG001`)

### Backward Compatibility
- Existing users with applied skins/backgrounds will automatically have them marked as "purchased"
- 0-point items are always considered "owned"

### Performance Considerations
- Purchase status is loaded once on page load
- Subsequent operations update local state without full reload
- WalletHistory queries use indexes on UserId and ItemCode

## Next Steps

1. **Manual File Edits**:
   - Copy methods from `PetService_NewMethods.cs` to `PetService.cs`
   - Add controller actions to `PetController.cs`
   - Update `Customize.cshtml` with new JavaScript

2. **Build & Test**:
   ```bash
   cd C:\Users\n2029\Desktop\work-1105\GamiPort\GamiPort
   dotnet build
   ```

3. **Run Application**:
   ```bash
   dotnet run
   ```

4. **Test All Scenarios** (see Testing Checklist above)

5. **Commit Changes**:
   - Follow project commit guidelines
   - Max 3 files or 400 lines per commit

## Support & Troubleshooting

### Issue: Background still shows purple gradient
**Solution**: Check browser console for image load errors. Verify file path in `wwwroot/MiniGame/PetBackgroundCostSettings表格_種子資料_圖片/`

### Issue: "已購買" not showing
**Solution**: Clear browser cache and reload. Check `GetPurchaseStatus` API response in Network tab.

### Issue: Points not deducting
**Solution**: Check WalletHistory table for transaction records. Verify transaction commit in logs.

### Issue: Can purchase same item twice
**Solution**: Verify `GetPurchasedSkinColorsAsync` / `GetPurchasedBackgroundsAsync` implementation. Check WalletHistory query filters.

