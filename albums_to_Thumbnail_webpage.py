import os

# 設定支援的照片格式
EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

def generate_html():
    subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    
    # 1. 主索引頁 (略，與上次相同)
    index_content = """
    <html><head><meta charset="UTF-8"><title>照片目錄</title>
    <style>
        body { font-family: "Microsoft JhengHei", sans-serif; padding: 40px; background: #dcdcdc; }
        .folder-card { background:white ; padding: 20px; margin: 10px; border-radius: 8px; 
                      box-shadow: 0 2px 5px rgba(0,0,0,0.1); display: inline-block; width: 220px; 
                      text-decoration: none; color: #333; text-align: center; font-weight: bold; }
        .folder-card:hover { transform: translateY(-5px); transition: 0.3s; background: #e0e0e0; }
    </style></head><body><h1>相簿總覽 /ᐠ .ᆺ. ᐟ\ﾉ     {:̲̅:̲̅:̲̅:̲̅{ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅ ̲̅{}ڪڪ       /ᐠ｡ꞈ｡ᐟ\ </h1><hr>
    """

    for folder in subdirs:
        photos = [f for f in os.listdir(folder) if f.lower().endswith(EXTENSIONS)]
        if not photos: continue

        index_content += f'<a class="folder-card" href="{folder}.html">📁 {folder}<br>({len(photos)} 張照片)</a>'

        # 2. 修改後的子頁面 (加入 Lightbox 功能)
        detail_content = f"""
        <html><head><meta charset="UTF-8"><title>{folder}</title>
        <style>
            body {{ font-family: "Microsoft JhengHei", sans-serif; text-align: center; background: #1a1a1a; color: white; margin: 0; }}
            .header {{ padding: 20px; background: #333; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px; padding: 20px; }}
            .img-container {{ background: #2a2a2a; padding: 10px; border-radius: 4px; transition: 0.2s; cursor: pointer; }}
            .img-container:hover {{ background: #3a3a3a; }}
            img.thumb {{ width: 100%; height: 200px; object-fit: cover; border-radius: 2px; }}
            p {{ font-size: 12px; margin-top: 8px; color: #bbb; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
            
            /* 彈窗(Modal) 樣式 */
            #modal {{ display: none; position: fixed; z-index: 1000; left: 0; top: 0; width: 100%; height: 100%; 
                     background-color: rgba(0,0,0,0.9); cursor: zoom-out; align-items: center; justify-content: center; }}
            #modal-img {{ max-width: 90%; max-height: 90%; object-fit: contain; cursor: default; }}
            .back-btn {{ display: inline-block; margin-bottom: 10px; color: #4CAF50; text-decoration: none; font-size: 14px; }}
        </style></head><body>
        
        <div class="header">
            <a href="index.html" class="back-btn">← 返回資料夾清單</a>
            <h1>{folder}</h1>
        </div>

        <div class="grid">
        """
        
        for p in photos:
            # 點擊縮圖時觸發 openModal()
            detail_content += f'''
            <div class="img-container" onclick="openModal('{folder}/{p}')">
                <img class="thumb" src="{folder}/{p}">
                <p>{p}</p>
            </div>'''
        
        # 加入 Modal 的 HTML 與 JavaScript 邏輯
        detail_content += """
        </div>

        <div id="modal" onclick="closeModal()">
            <img id="modal-img" src="" onclick="event.stopPropagation()">
        </div>

        <script>
            function openModal(src) {
                document.getElementById('modal').style.display = 'flex';
                document.getElementById('modal-img').src = src;
                document.body.style.overflow = 'hidden'; // 禁止背景捲動
            }

            function closeModal() {
                document.getElementById('modal').style.display = 'none';
                document.getElementById('modal-img').src = '';
                document.body.style.overflow = 'auto'; // 恢復背景捲動
            }

            // 支援按下 Esc 鍵關閉
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') closeModal();
            });
        </script>
        </body></html>
        """
        
        with open(f"{folder}.html", "w", encoding="utf-8") as f:
            f.write(detail_content)

    index_content += "</body></html>"
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print("✅ 網頁已更新！現在具備點擊大圖與空白處關閉功能。")

if __name__ == "__main__":
    generate_html()