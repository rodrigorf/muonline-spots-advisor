import win32gui
import win32ui
import win32con

class WindowsEngine:
    def get_screen_executable(self, executable_name, save_path=None):
        hwnd = win32gui.FindWindow(None, executable_name)
        if hwnd:
            # Step 2: Get the full dimensions of the window, including non-client area
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            width = right - left
            height = bottom - top
            
            # Step 3: Get the client dimensions of the window, which excludes the non-client area
            left_border, top_border, right_border, bottom_border = win32gui.GetClientRect(hwnd)
            client_width = right_border - left_border
            client_height = bottom_border - top_border
            
            # Step 4: Calculate the offset between client area and full area, and adjust left and top coordinates accordingly
            left_offset = (width - client_width) // 2
            top_offset = height - client_height - left_offset
            left += left_offset
            top += top_offset
            
            # Step 5: Capture screenshot of the identified window using adjusted dimensions
            hwindc = win32gui.GetWindowDC(hwnd)
            srcdc = win32ui.CreateDCFromHandle(hwindc)
            memdc = srcdc.CreateCompatibleDC()
            bmp = win32ui.CreateBitmap()
            bmp.CreateCompatibleBitmap(srcdc, client_width, client_height)
            memdc.SelectObject(bmp)
            memdc.BitBlt((0, 0), (client_width, client_height), srcdc, (left_offset, top_offset), win32con.SRCCOPY)
            
            # Step 6: If save path is provided, save image to specified location
        if save_path:
            bmp.SaveBitmapFile(memdc, save_path)
    
        return None


