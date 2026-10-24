# 專案進度與交接 (PROGRESS.md)

最後更新：2026-10-24（home）

## 目前階段
**專案清理與標準化完成！舊版過渡檔案已清除，完整保留 9:16 直式架構、Breeze TTS 2 語音方案與最新短片成品。**

## 使用者已確認的事
- 2026-10-23：確認使用 `shanshiba-workflow-colab` 雲端版本。
- 2026-10-24：**遠端最新功能同步**（多角色同鏡對話、50~120字 Action 結構、純文字讀本估算、遠景小臉精修等）。
- 2026-10-24：**Codex CLI 生圖技能啟用**（建立 `codex.cmd` 轉發檔，走 ChatGPT 方案免 Key 生圖）。
- 2026-10-24：**語音升級至 Breeze TTS 2（方案 C）**：在 Colab 生成三位角色聲音（陳工、老李、阿強），使用者試聽通過。
- 2026-10-24：**直式管線全面打通**：
  - 升級 `make_film.py` 與 `render_ending.py` 支援原生 9:16 直式。
  - 14 鏡直式首幀透過 H3 成功生成原生 768×1344 影片。
  - S11 與 S14 經獨立換 seed 重抽後全數通過台詞聽寫檢驗。
  - 完成 MiniMax Music 3 純器樂配樂合成、1080×1920 剪輯、直式片尾動畫與繁體中文字幕疊加。
  - 自審五遍全部 PASS（響度 −15.8 LUFS、無黑畫面、無台詞被切斷問題）。
  - **最新直式成片**：`pipeline/typhoon_bonus/out/cut/film_1080p.mp4`（96.17 秒，1080×1920 @ 24fps）。
- 2026-10-24：**安全關機**：依使用者指示執行 `python cloud/colab_h3.py stop`，安全關閉虛擬機（剩餘 **375.08 運算單元**，停止計費）。
- 2026-10-24：**專案清理與精簡**：
  - 刪除舊版過渡用的 Edge-TTS 腳本（`tools/make_edge_voices.py`）。
  - 清理舊版 16:9 橫式暫存備份（釋放 843 MB 磁碟空間）。
  - 統一範本與專案的 `make_film.py`（直式/橫式自適應、配樂長度不足自動延伸、剪輯點對齊 1/24 秒）。
  - 補強 `.gitignore`（忽略快取、大檔、備份與壓縮包）。
- 2026-10-24：**個人 GitHub 倉庫建立與同步**：將專案完整推送至 [erniesu8090-beep/AI-Moive-ByColab](https://github.com/erniesu8090-beep/AI-Moive-ByColab)，並將 `origin` 設為該倉庫（原母專案保留為 `upstream_colab`）。

## 待使用者決定
1. 第二部全新影片的主題與劇本規劃（可使用 `shanshiba-drama` 技能與 `codex-imagegen-bridge` 快速建置角色與分鏡）。

## 接手須知
- **最新直式成片路徑**：`pipeline/typhoon_bonus/out/cut/film_1080p.mp4`
- **啟動 Colab 指令**：`python cloud/colab_h3.py start`
- **關閉 Colab 指令**：`python cloud/colab_h3.py stop`
- **當前餘額**：375.08 運算單元（消耗率 0.00/hr）。

## 修訂紀錄
- 2026-10-23｜home｜下載專案、修補 Colab CLI、打通第一部橫式短片。
- 2026-10-24｜home｜同步 4 個最新 Commits、解鎖 Codex 生圖技能、配置 Breeze TTS 2、重構直式 9:16 管線、產出正式 1080×1920 直式成片並安全關機；完成專案精簡與冗餘清理。
- 2026-10-24｜home｜設定遠端 origin 為 erniesu8090-beep/AI-Moive-ByColab 並完成初始推送。
