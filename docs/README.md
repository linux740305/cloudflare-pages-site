# nyxveil

這個資料夾已經整理成 `nyxveil` 的 Cloudflare Pages 專案結構。

## 目前結構

- `site/index.html`：公開首頁
- `docs/`：內部說明文件，不應作為網站公開內容

## 部署方式

1. 把這個資料夾放進 GitHub repository。
2. 到 Cloudflare Pages 建立新專案。
   建議專案名稱使用 `nyxveil`。
3. 連接該 repository。
4. 如果是目前這種純靜態網站：
   - `Build command` 留空
   - `Build output directory` 使用 `site`
5. 部署完成後即可取得免費預設網址，預期會像 `https://nyxveil.pages.dev`。

## 本機修改

直接編輯 `site/index.html` 即可。
