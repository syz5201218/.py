import pygame
import sys

# 1. 初始化Pygame
pygame.init()

# 2. 建立遊戲視窗（寬800像素，高600像素）
screen = pygame.display.set_mode((800, 600))

# 3. 設定視窗標題
pygame.display.set_caption("我的第一個Pygame遊戲")

# 4. 設定視窗背景顏色（RGB值）
background_color = (135, 206, 235)  # 天藍色

# 5. 遊戲主循環
running = True
while running:
    # 6. 處理事件
    for event in pygame.event.get():
        # 如果點擊視窗關閉按鈕
        if event.type == pygame.QUIT:
            running = False
    
    # 7. 填滿背景顏色
    screen.fill(background_color)
    
    # 8. 顯示一些文字（這是你可以做的額外功能）
    font = pygame.font.Font(None, 36)  # 使用預設字體，大小36
    text = font.render("Hello Pygame!", True, (255, 255, 255))  # 白色文字
    screen.blit(text, (300, 280))  # 在(300, 280)位置顯示文字
    
    # 9. 更新畫面顯示
    pygame.display.flip()

# 10. 退出遊戲
pygame.quit()
sys.exit()
