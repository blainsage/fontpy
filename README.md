# fontpy
python script to convert fonts to cpp header files
# ImGui Font Example

This project demonstrates how to **embed a TTF font directly in your C++ application** and use it in ImGui without relying on external font files.  

In this example, we use **Impact.ttf**, embedded as a byte array in `impact_font.h`.

---

## Features

- Load a font from memory (`AddFontFromMemoryTTF`)
- No external font files required
- Works cross-platform
- Simple fallback/error handling

---

## Files

- `impact_font.h` — The embedded TTF file exported as a byte array
- `main.cpp` — Example usage with ImGui

---

## How It Works

1. Include the font header:

```cpp
#include "impact_font.h"
----------------------------------
ImGuiIO& io = ImGui::GetIO();
----------------------------------


ImFont* font = io.Fonts->AddFontFromMemoryTTF(
    impact_ttf,        // pointer to memory
    impact_ttf_size,   // size of memory
    16.0f              // font size in pixels
);
----------------------------------
if (!font) {
    // fallback to default font or log an error
    font = io.Fonts->Fonts[0]; // default ImGui font
}
