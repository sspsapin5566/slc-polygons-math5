import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs("output/images", exist_ok=True)

# Helper function to get font
def get_font(size):
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

font_title = get_font(32)
font_body = get_font(22)
font_large = get_font(44)

# Color Palette: Learning Community (Matcha Green Theme)
BG_COLOR = (238, 242, 235)      # Matcha Cream
PRIMARY_COLOR = (35, 65, 45)    # Deep Pine Green
ACCENT_COLOR = (190, 75, 20)    # Terracotta / Amber Highlight
TEXT_COLOR = (50, 60, 50)       # Dark Slate Green
CARD_BG = (255, 255, 255)       # Pure White Card
LINE_COLOR = (120, 150, 125)    # Soft Sage Green

slides_info = [
    {
        "filename": "output/images/slide_1.png",
        "badge": "觀課分析報告",
        "title": "認識多邊形 公開課",
        "subtitle": "文林國小 黃曉雯老師 五年級數學",
        "draw_func": "title_card"
    },
    {
        "filename": "output/images/slide_2.png",
        "badge": "108 課綱對齊",
        "title": "幾何概念與素養導向",
        "subtitle": "數-E-A2 / 數-E-B1 / 數-E-C2",
        "draw_func": "curriculum_card"
    },
    {
        "filename": "output/images/slide_3.png",
        "badge": "活動一：直觀分類",
        "title": "生活圖形貼紙大分類",
        "subtitle": "平面圖形特徵觀察與歸類",
        "draw_func": "stickers_card"
    },
    {
        "filename": "output/images/slide_4.png",
        "badge": "活動二：核心定義",
        "title": "封閉圖形與全直線段",
        "subtitle": "排除圓弧與迷思概念釐清",
        "draw_func": "definition_card"
    },
    {
        "filename": "output/images/slide_5.png",
        "badge": "活動三：正多邊形",
        "title": "每邊一樣長・每角一樣大",
        "subtitle": "正三角形、正方形與正六邊形",
        "draw_func": "regular_card"
    },
    {
        "filename": "output/images/slide_6.png",
        "badge": "活動四：要素量化",
        "title": "邊數 N = 頂點數 = 角數",
        "subtitle": "五邊形：5邊 / 5頂點 / 5內角",
        "draw_func": "elements_card"
    },
    {
        "filename": "output/images/slide_7.png",
        "badge": "活動五：思考帽",
        "title": "附件14 卡紙交疊探究",
        "subtitle": "正方形與正六邊形圖形重疊",
        "draw_func": "overlay_card"
    },
    {
        "filename": "output/images/slide_8.png",
        "badge": "活動六：數位學習",
        "title": "均一教育平台適性挑戰",
        "subtitle": "即時診斷與個別化練習",
        "draw_func": "digital_card"
    },
    {
        "filename": "output/images/slide_9.png",
        "badge": "SLC 觀課反思",
        "title": "同儕共學與個別化鷹架",
        "subtitle": "傾聽對話・引導思考・同儕互助",
        "draw_func": "reflection_card"
    },
    {
        "filename": "output/images/slide_10.png",
        "badge": "行動建議",
        "title": "素養導向教學延伸與展望",
        "subtitle": "多邊形內角和與數學日記",
        "draw_func": "action_card"
    }
]

for item in slides_info:
    img = Image.new("RGB", (600, 600), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # White Card background with soft rounded shadow
    draw.rectangle([30, 30, 570, 570], fill=CARD_BG, outline=LINE_COLOR, width=3)
    
    # Top Decorative Banner
    draw.rectangle([30, 30, 570, 100], fill=PRIMARY_COLOR)
    draw.text((50, 48), item["badge"], font=font_title, fill=(255, 255, 255))
    
    # Header Titles
    draw.text((50, 125), item["title"], font=font_title, fill=PRIMARY_COLOR)
    draw.text((50, 170), item["subtitle"], font=font_body, fill=TEXT_COLOR)
    draw.line([(50, 205), (550, 205)], fill=ACCENT_COLOR, width=2)
    
    # Custom Graphic Content based on draw_func
    func = item["draw_func"]
    
    if func == "title_card":
        # Draw cute geometric icons
        draw.polygon([(150, 430), (300, 250), (450, 430)], fill=(220, 238, 225), outline=PRIMARY_COLOR, width=4)
        draw.rectangle([100, 450, 500, 530], fill=PRIMARY_COLOR)
        draw.text((120, 475), "學習共同體 SLC 課例研究", font=font_title, fill=(255, 255, 255))

    elif func == "curriculum_card":
        # 3 Badges
        draw.rounded_rectangle([60, 240, 210, 340], radius=15, fill=(230, 245, 235), outline=PRIMARY_COLOR, width=3)
        draw.text((80, 280), "數-E-A2\n系統思考", font=font_body, fill=PRIMARY_COLOR)
        
        draw.rounded_rectangle([225, 240, 375, 340], radius=15, fill=(255, 240, 230), outline=ACCENT_COLOR, width=3)
        draw.text((245, 280), "數-E-B1\n符號溝通", font=font_body, fill=ACCENT_COLOR)
        
        draw.rounded_rectangle([390, 240, 540, 340], radius=15, fill=(230, 245, 235), outline=PRIMARY_COLOR, width=3)
        draw.text((410, 280), "數-E-C2\n團隊合作", font=font_body, fill=PRIMARY_COLOR)

        # Polygon shapes below
        draw.polygon([(150, 500), (200, 390), (250, 500)], outline=PRIMARY_COLOR, width=4) # Triangle
        draw.rectangle([290, 400, 390, 500], outline=PRIMARY_COLOR, width=4)               # Quad
        draw.polygon([(440, 440), (470, 390), (520, 430), (500, 490), (450, 490)], outline=ACCENT_COLOR, width=4) # Pentagon

    elif func == "stickers_card":
        # Sticker board simulation
        draw.rectangle([70, 230, 270, 530], fill=(245, 248, 244), outline=PRIMARY_COLOR, width=3)
        draw.text((90, 245), "✅ 多邊形", font=font_title, fill=PRIMARY_COLOR)
        draw.polygon([(120, 360), (220, 360), (170, 290)], fill=(200, 230, 205))
        draw.rectangle([120, 400, 220, 490], fill=(200, 230, 205))

        draw.rectangle([330, 230, 530, 530], fill=(255, 245, 245), outline=ACCENT_COLOR, width=3)
        draw.text((350, 245), "❌ 非多邊形", font=font_title, fill=ACCENT_COLOR)
        draw.ellipse([370, 300, 470, 400], fill=(255, 215, 215)) # Circle
        draw.text((380, 440), "含曲線/圓弧", font=font_body, fill=ACCENT_COLOR)

    elif func == "definition_card":
        # Two Key Rules
        draw.rounded_rectangle([70, 240, 530, 360], radius=15, fill=(235, 245, 238), outline=PRIMARY_COLOR, width=3)
        draw.text((100, 270), "要件 1：必須是「封閉圖形」", font=font_title, fill=PRIMARY_COLOR)
        draw.text((100, 315), "首尾相接，內部無開口", font=font_body, fill=TEXT_COLOR)

        draw.rounded_rectangle([70, 390, 530, 510], radius=15, fill=(235, 245, 238), outline=PRIMARY_COLOR, width=3)
        draw.text((100, 420), "要件 2：全由「直線段」組成", font=font_title, fill=PRIMARY_COLOR)
        draw.text((100, 465), "無任何圓弧或曲線段", font=font_body, fill=TEXT_COLOR)

    elif func == "regular_card":
        # Equilateral Triangle
        draw.polygon([(140, 360), (70, 480), (210, 480)], fill=(220, 240, 225), outline=PRIMARY_COLOR, width=4)
        draw.text((95, 500), "正三角形", font=font_body, fill=PRIMARY_COLOR)

        # Square
        draw.rectangle([250, 360, 370, 480], fill=(220, 240, 225), outline=PRIMARY_COLOR, width=4)
        draw.text((285, 500), "正方形", font=font_body, fill=PRIMARY_COLOR)

        # Regular Hexagon
        draw.polygon([(470, 350), (530, 390), (530, 450), (470, 490), (410, 450), (410, 390)], fill=(255, 235, 225), outline=ACCENT_COLOR, width=4)
        draw.text((435, 500), "正六邊形", font=font_body, fill=ACCENT_COLOR)

    elif func == "elements_card":
        # Pentagon diagram with vertices labeled
        pts = [(300, 250), (450, 340), (400, 490), (200, 490), (150, 340)]
        draw.polygon(pts, fill=(235, 245, 240), outline=PRIMARY_COLOR, width=5)
        
        # Red dots for vertices
        for pt in pts:
            draw.ellipse([pt[0]-10, pt[1]-10, pt[0]+10, pt[1]+10], fill=ACCENT_COLOR)
            
        draw.text((180, 520), "5 個邊 ＝ 5 個頂點 ＝ 5 個內角", font=font_title, fill=PRIMARY_COLOR)

    elif func == "overlay_card":
        # Square & Hexagon overlay
        draw.rectangle([150, 260, 350, 460], outline=PRIMARY_COLOR, width=4)
        draw.polygon([(300, 230), (420, 280), (420, 420), (300, 470), (180, 420), (180, 280)], outline=ACCENT_COLOR, width=4)
        draw.text((120, 500), "附件14 卡紙交疊 ➔ 拼出多種多邊形", font=font_title, fill=PRIMARY_COLOR)

    elif func == "digital_card":
        # Tablet screen graphic
        draw.rounded_rectangle([100, 230, 500, 480], radius=20, fill=(240, 245, 250), outline=PRIMARY_COLOR, width=5)
        draw.rectangle([130, 260, 470, 450], fill=(255, 255, 255))
        draw.text((160, 280), "均一教育平台 均一挑戰", font=font_title, fill=PRIMARY_COLOR)
        draw.text((160, 330), "✔ 任務 1：多邊形辨識 (通過)", font=font_body, fill=(40, 140, 60))
        draw.text((160, 370), "✔ 任務 2：邊角數量計算 (通過)", font=font_body, fill=(40, 140, 60))
        draw.text((180, 500), "平板適性練習與即時診斷", font=font_title, fill=ACCENT_COLOR)

    elif func == "reflection_card":
        # Discussion circle
        draw.ellipse([150, 260, 450, 460], outline=PRIMARY_COLOR, width=4)
        draw.text((220, 345), "同儕共學\n傾聽與對話", font=font_title, fill=PRIMARY_COLOR)
        draw.ellipse([120, 240, 180, 300], fill=ACCENT_COLOR)
        draw.ellipse([420, 240, 480, 300], fill=ACCENT_COLOR)
        draw.ellipse([270, 430, 330, 490], fill=ACCENT_COLOR)
        draw.text((130, 520), "SLC 高品質課堂研究：觀課與議課反思", font=font_title, fill=PRIMARY_COLOR)

    elif func == "action_card":
        # Action plan checklist
        draw.rounded_rectangle([70, 230, 530, 520], radius=15, fill=(245, 250, 245), outline=PRIMARY_COLOR, width=3)
        draw.text((100, 260), "📌 行動建議一：凹多邊形標註練習", font=font_body, fill=PRIMARY_COLOR)
        draw.text((100, 320), "📌 行動建議二：連結多邊形內角和推理", font=font_body, fill=PRIMARY_COLOR)
        draw.text((100, 380), "📌 行動建議三：數學思考日記寫作", font=font_body, fill=PRIMARY_COLOR)
        draw.text((100, 440), "🌟 達成素養導向幾何推理學習目標", font=font_title, fill=ACCENT_COLOR)

    img.save(item["filename"])
    print(f"[OK] Generated slide illustration: {item['filename']}")

print("All 10 slide images generated successfully!")
