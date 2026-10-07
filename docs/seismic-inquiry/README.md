# 校園折射震測 × 科學建模 教學網站

> **備註：** 本資料夾已併入「地球物理通論」課堂頁倉庫的 GitHub Pages（`docs/seismic-inquiry/`），網址為 `…/2026_Utaipei_Geophysics_0909/seismic-inquiry/`。下方的「部署到 GitHub Pages」步驟是此網站獨立部署時的說明，在本倉庫中不需要再做。

這是一個可直接部署到 **GitHub Pages** 的純靜態網站。

## 內容
- 完整納入本次對話提供的 **60 張現場照片**
- 12 個震源點：0–44 m，每 4 m 一點
- 實驗流程：儀器 → 量距 → 受波器 → 接線 → 震源 → 取樣 → 波形 → first arrival → 多震源觀測 → 場地復原
- 互動式震源位置／source–receiver distance 練習
- 互動式兩層速度模型與 travel-time curve
- CER 科學論證與科學建模收束
- 現場影片（assets/video/1000050534.mp4）

## 部署到 GitHub Pages
1. 建立新的 GitHub repository。
2. 將此資料夾內的所有檔案上傳到 repository 根目錄。
3. 進入 **Settings → Pages**。
4. 在 **Build and deployment** 選擇 `Deploy from a branch`。
5. Branch 選 `main`，Folder 選 `/ (root)`，儲存。
6. 等待 GitHub 產生網站網址。

## 檔案結構
```text
index.html
style.css
script.js
.nojekyll
assets/
  images/   # 60 張現場照片
  video/    # 現場影片
```

## 修改文字
主要教學內容都在 `index.html`；版面在 `style.css`；互動功能在 `script.js`。

## 備註
互動式兩層模型中的速度與深度是「教學示意參數」，網站已明確標示不代表本次實測反演結果。
