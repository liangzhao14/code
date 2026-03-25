---
source: https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors/small-modular-reactor-smr-design-database
downloaded: 2026-03-24 23:57:17
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [nuclear power reactors](https://world-nuclear.org/information-library/nuclear-power-reactors) / [small-modular-reactors](https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors) / Small Modular Reactor (SMR) Design Database

nuclear power reactors

# Small Modular Reactor (SMR) Design Database

Updated Wednesday, 18 February 2026

(function() {
// Create all HTML
var container = document.getElementById('smr-app-container');
container.innerHTML = '<style>' +
'\* { margin: 0; padding: 0; box-sizing: border-box; }' +
'#smr-app-container { font-family: "Muli", Arial, sans-serif; background: transparent; color: #212529; }' +
'#smr-app-container p { margin: 0; padding: 0; }' +
'#smr-app-container h1, #smr-app-container h2, #smr-app-container h3, #smr-app-container h4 { margin: 0; padding: 0; }' +
'.smr-tabs-wrapper { background: white; border-bottom: 1px solid #e5e7eb; padding: 0 32px; }' +
'.smr-tabs { display: flex; gap: 0; }' +
'.smr-tab { padding: 16px 24px; background: none; border: none; border-bottom: 3px solid transparent; font-size: 15px; font-weight: 600; color: #6b7280; cursor: pointer; transition: all 0.2s; }' +
'.smr-tab:hover { color: #374151; }' +
'.smr-tab.active { color: #212529; border-bottom-color: #6a8ec9; }' +
'.smr-tab-content { display: none; }' +
'.smr-tab-content.active { display: block; }' +
'.smr-about-content { max-width: 800px; margin: 0 auto; padding: 48px 32px; }' +
'.smr-about-content p { font-size: 16px; line-height: 1.6; color: #374151; text-align: left; }' +
'.smr-container { display: flex; min-height: 100vh; }' +
'.smr-sidebar {width: 280px; background: #fff; padding: 0; border-right: 1px solid #e5e7eb; overflow-y: auto; position: sticky; top: 0; height: 100vh; display: flex; flex-direction: column; padding-top: 32px; }' +
'.smr-sidebar.hidden { display: none; }' +
// Sticky header styles
'.smr-sidebar-header { position: sticky; top: 0; background: #fff; border-bottom: 1px solid #e5e7eb; padding: 12px 16px; z-index: 10; flex-shrink: 0; }' +
'.smr-sidebar-header-buttons { display: flex; gap: 8px; justify-content: space-between; }' +
'.smr-close-sidebar-btn { flex: 1; padding: 10px 16px; background: #6b7280; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 600; transition: background 0.2s; font-family: inherit; }' +
'.smr-close-sidebar-btn:hover { background: #4b5563; }' +
'.smr-reset-all-btn { flex: 1; padding: 10px 16px; background: #6a8ec9; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 600; transition: background 0.2s; font-family: inherit; }' +
'.smr-reset-all-btn:hover { background: #5677a9; }' +
// Sidebar content wrapper
'.smr-sidebar-content { flex: 1; overflow-y: auto; padding: 16px; }' +
// Off-canvas overlay
'.smr-sidebar-overlay { display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0, 0, 0, 0.5); z-index: 998; opacity: 0; transition: opacity 0.3s ease; }' +
'.smr-sidebar-overlay.active { display: block; opacity: 1; }' +
'.smr-search-section { margin-bottom: 24px; }' +
'.smr-search-section-mobile { display: none; }' +
'.smr-reset-btn { background: none; border: none; color: #6a8ec9; font-size: 13px; cursor: pointer; padding: 0; text-decoration: none; font-family: inherit; }' +
'.smr-reset-btn:hover { text-decoration: underline; }' +
'.smr-filter-section { margin-bottom: 0; }' +
'.smr-filter-section h3 { font-size: 13px; font-weight: 600; color: #6b7280; margin: 0 0 8px 0; padding: 0; display: block; line-height: 1.2; }' +
'.smr-search-box { width: 100%; padding: 10px 12px; border: 1px solid #d1d5db; border-radius: 999px; font-size: 15px; background-color: white; font-family: inherit; }' +
'.smr-search-box:focus { outline: none; border-color: #6a8ec9; box-shadow: 0 0 0 3px rgba(106, 142, 201, 0.1); }' +
'.smr-checkbox-group { display: flex; flex-direction: column; gap: 6px; margin: 0; padding: 8px 0 0 20px; }' +
'.smr-checkbox-group label { display: flex; align-items: center; padding: 4px 0; cursor: pointer; font-size: 14px; color: #374151; border: none; background: none; transition: background 0.15s; margin: 0; line-height: 1.2; }' +
'.smr-checkbox-group label:hover { background: #f9fafb; }' +
'.smr-checkbox-group input[type="checkbox"] { margin: 0 10px 0 0; width: 18px; height: 18px; accent-color: #6a8ec9; flex-shrink: 0; }' +
'.smr-multiselect { width: 100%; padding: 8px 10px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; background-color: #ffffff; margin: 0; font-family: inherit; }' +
'.smr-multiselect:focus { outline: none; border-color: #6a8ec9; box-shadow: 0 0 0 3px rgba(106, 142, 201, 0.1); }' +
'.smr-range-inputs { display: flex; gap: 8px; margin-top: 6px; padding: 8px 0 0 20px; }' +
'.smr-range-input-wrapper { flex: 1; }' +
'.smr-range-input-wrapper label { display: block; font-size: 11px; color: #6b7280; margin: 0 0 4px 0; padding: 0; font-weight: 500; line-height: 1.2; }' +
'.smr-range-input-wrapper input { width: 100%; padding: 8px 10px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 13px; margin: 0; }' +
'.smr-range-input-wrapper input:focus { outline: none; border-color: #6a8ec9; box-shadow: 0 0 0 3px rgba(106, 142, 201, 0.1); }' +
'.smr-main-content { flex: 1; padding: 32px; }' +
'.smr-main-content.full-width { width: 100%; max-width: 100%; }' +
'.smr-results-header { margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; }' +
'.smr-results-count { font-size: 14px; color: #6c757d; }' +
'.smr-sort-wrapper { display: flex; align-items: center; gap: 8px; }' +
'.smr-sort-wrapper label { font-size: 14px; color: #6b7280; font-weight: 500; }' +
'.smr-sort-select { padding: 8px 12px; border: 1px solid #d1d5db; border-radius: 6px; font-size: 14px; background: white; cursor: pointer; }' +
'.smr-sort-select:focus { outline: none; border-color: #6a8ec9; box-shadow: 0 0 0 3px rgba(106, 142, 201, 0.1); }' +
'.smr-active-filters-wrapper { margin-bottom: 16px; display: flex; align-items: flex-start; gap: 8px; flex-wrap: wrap; }' +
'.smr-filter-chips-container { display: flex; flex-wrap: wrap; gap: 8px; flex: 1; align-items: center; }' +
'.smr-filter-chip { display: inline-flex; align-items: center; gap: 6px; padding: 6px 12px; background: #ffffff; color: #1f3b7b; border: 1px solid #6a8ec9; border-radius: 16px; font-size: 13px; font-weight: 500; }' +
'.smr-chip-remove { background: none; border: none; color: #6a8ec9; padding: 0; margin: 0; font-size: 16px; line-height: 1; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; width: 16px; height: 16px; }' +
'.smr-chip-remove:hover { color: #5677a9; }' +
'.smr-active-clear-btn { background: none; border: none; color: #6a8ec9; cursor: pointer; padding: 6px 12px; text-decoration: none; white-space: nowrap; font-weight: 500; font-family: inherit; }' +
'.smr-active-clear-btn:hover { text-decoration: underline; }' +
'.smr-compare-bar { display:none; align-items:center; gap:12px; padding:10px 12px; background:#ffffff; border:1px solid #e5e7eb; border-radius:8px; margin-bottom:16px; }.smr-compare-list { display:flex; flex-wrap:wrap; gap:8px; }.smr-compare-chip { display:inline-flex; align-items:center; gap:6px; padding:6px 10px; background:#f9fafb; border:1px solid #d1d5db; border-radius:999px; font-size:12px; }.smr-compare-chip button { background:none; border:none; cursor:pointer; color:#6b7280; font-size:14px; line-height:1; }.smr-compare-btn { padding:8px 14px; background:#6a8ec9; color:#fff; border:none; border-radius:6px; font-weight:600; cursor:pointer; }.smr-compare-btn:disabled { opacity:0.5; cursor:not-allowed; }.smr-compare-select { display:flex; align-items:center; gap:6px; margin-bottom:8px; font-size:12px; color:#6b7280; }' +
// Loading state for results grid
'.smr-results-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; transition: opacity 0.2s ease; }' +
'.smr-results-grid.loading { pointer-events: none; }' +
'.smr-skeleton-card { position: relative; overflow: hidden; }' +
'.smr-skeleton-title, .smr-skeleton-badge, .smr-skeleton-line, .smr-skeleton-button {' +
'display: block;' +
'background: linear-gradient(90deg, #f3f4f6, #e5e7eb, #f3f4f6);' +
'background-size: 200px 100%;' +
'animation: smr-skeleton-loading 1.2s ease-in-out infinite;' +
'}' +
'.smr-skeleton-title { height: 20px; width: 60%; border-radius: 4px; margin-bottom: 12px; }' +
'.smr-skeleton-badge { height: 20px; width: 72px; border-radius: 999px; }' +
'.smr-skeleton-line { height: 12px; width: 100%; border-radius: 4px; margin-bottom: 6px; }' +
'.smr-skeleton-line.short { width: 60%; }' +
'.smr-skeleton-button { height: 32px; width: 100%; border-radius: 6px; margin-top: 12px; }' +
'@keyframes smr-skeleton-loading { 0% { background-position: -200px 0; } 100% { background-position: calc(200px + 100%) 0; } }' +
'.smr-reactor-card { background: white; border: 1px solid #dee2e6; border-radius: 8px; padding: 20px; transition: all 0.2s; }' +
'.smr-reactor-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); transform: translateY(-2px); }' +
'.smr-reactor-name { font-size: 18px; font-weight: 600; color: #212529; margin-bottom: 12px; }' +
'.smr-reactor-meta { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; }' +
'.smr-badge { padding: 4px 10px; background: #e7f1ff; color: #6a8ec9; border-radius: 12px; font-size: 12px; font-weight: 500; }' +
'.smr-reactor-details { font-size: 13px; color: #6c757d; line-height: 1.6; }' +
'.smr-reactor-details div { margin-bottom: 4px; }' +
'.smr-detail-btn { margin-top: 12px; padding: 8px 16px; background: #6a8ec9; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 500; width: 100%; font-family: inherit; }' +
'.smr-detail-btn:hover { background: #5677a9; }' +
'.smr-detail-view { display: none; background: white; border: 1px solid #dee2e6; border-radius: 8px; padding: 20px; }' +
'.smr-detail-view.active { display: block; }' +
'.smr-detail-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; }' +
'.smr-detail-title { font-size: 18px; font-weight: 600; color: #212529; }' +
'.smr-back-btn { padding: 8px 16px; background: #6b7280; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 500; font-family: inherit; }' +
'.smr-back-btn:hover { background: #4b5563; }' +
'.smr-detail-content { display: flex; flex-direction: column; gap: 20px; }' +
'.smr-detail-meta { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 12px; }' +
'.smr-detail-specs { font-size: 13px; color: #6c757d; line-height: 1.6; }' +
'.smr-detail-specs > div { margin-bottom: 4px; }' +
'.smr-application-inline { display: inline-flex; align-items: center; gap: 4px; margin-right: 12px; white-space: nowrap; }' +
'.smr-application-inline-icon { font-size: 14px; font-weight: bold; }' +
'.smr-application-inline-icon.yes { color: #10b981; }' +
'.smr-application-inline-icon.no { color: #9ca3af; }' +
'.smr-detail-notes-heading { font-size: 13px; font-weight: 600; margin-top: 16px; margin-bottom: 4px; color: #6c757d; }' +
'.smr-notes-content { font-size: 13px; line-height: 1.6; color: #6c757d; white-space: pre-line; }' +
'.smr-notes-content p, .smr-notes-content span, .smr-notes-content li { font-size: 13px !important; line-height: 1.6; color: #6c757d; margin: 12px 0 12px 0 !important; }' +
'.smr-no-results { text-align: center; padding: 60px 20px; color: #6c757d; }' +
'.smr-mobile-filter-toggle { display: none; margin-bottom: 12px; padding: 8px 12px; background: #e5e7eb; border: 1px solid #d1d5db; border-radius: 6px; font-size: 14px; font-weight: 500; color: #374151; cursor: pointer; }' +
'.smr-mobile-filter-toggle:hover { background: #d1d5db; }' +
'.smr-filter-toggle { cursor: pointer; display: flex; justify-content: space-between; align-items: center; font-size: 14px; font-weight: 400; color: #000; margin: 0; padding: 10px 0; line-height: 1.2; border-bottom: 1px solid #e5e7eb; }' +
'.smr-arrow { font-size: 10px; color: #666; transition: transform 0.3s ease; }' +
'.smr-arrow.expanded { transform: rotate(180deg); }' +
/\* Summary tab + charts \*/
'.smr-summary-content { padding: 0; max-width: 1000px; margin: 0; }' +
'.smr-summary-intro { font-size: 15px; color: #4b5563; margin-bottom: 24px; }' +
'.smr-chart-area-title { font-weight: 800; font-size: 16px; line-height: 1.3; color: #111827; margin-bottom: 24px; }' +
'.smr-histogram-area-title { font-weight: 800; font-size: 16px; line-height: 1.3; color: #111827; margin-bottom: 24px; margin-top: 32px; }' +
'.smr-summary-stat { margin-bottom: 16px; padding: 16px; background: transparent; border: 1px solid #e2e8f0; border-radius: 8px; text-align: left; transition: all 0.2s ease; }' +
'.smr-summary-stat:hover { background: #f9fafb; border-color: #cbd5e1; transform: translateY(-1px); }' +
'.smr-stat-number { font-weight: 800; font-size: 28px; line-height: 1; color: #111827; }' +
'.smr-stat-label { font-weight: 500; font-size: 14px; line-height: 1.2; color: #6b7280; margin-top: 2px; }' +
'.smr-summary-left { position: absolute; top: 0; left: 0; width: 280px; padding: 48px 32px 0 32px; text-align: right; font-weight: 800; font-size: 16px; line-height: 1.3; color: #111827; }' +
// Updated chart styles for tabbed interface
'.smr-chart-container { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 0; overflow: hidden; width: 100%; max-width: 660px; margin: 0; }' +
'.smr-chart-tabs { display: flex; background: white; border-bottom: 1px solid #e5e7eb; gap: 0; }' +
'.smr-chart-tab { padding: 16px 20px; background: none; border: none; border-bottom: 3px solid transparent; font-size: 14px; font-weight: 600; color: #6b7280; cursor: pointer; transition: all 0.2s; text-align: center; flex: 1; }' +
'.smr-chart-tab:hover { color: #374151; }' +
'.smr-chart-tab.active { color: #212529; border-bottom-color: #6a8ec9; }' +
'.smr-chart-content { padding: 18px; }' +
// Histogram container styles
'.smr-histogram-container { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 0; overflow: hidden; width: 100%; max-width: 660px; margin: 0; }' +
'.smr-histogram-tabs { display: flex; background: white; border-bottom: 1px solid #e5e7eb; gap: 0; }' +
'.smr-histogram-tab { padding: 16px 20px; background: none; border: none; border-bottom: 3px solid transparent; font-size: 14px; font-weight: 600; color: #6b7280; cursor: pointer; transition: all 0.2s; text-align: center; flex: 1; }' +
'.smr-histogram-tab:hover { color: #374151; }' +
'.smr-histogram-tab.active { color: #212529; border-bottom-color: #6a8ec9; }' +
'.smr-histogram-content { padding: 18px; }' +
// Vertical histogram styles
'.smr-histogram-chart { display: flex; align-items: flex-end; height: 200px; gap: 8px; padding: 30px 0 40px 0; }' +
'.smr-histogram-bar-container { flex: 1; display: flex; flex-direction: column; align-items: center; height: 100%; justify-content: flex-end; position: relative; }' +
'.smr-histogram-bar { background: #6a8ec9; width: 100%; border-radius: 4px 4px 0 0; transition: background 0.2s; min-height: 2px; }' +
'.smr-histogram-bar:hover { background: #5677a9; }' +
'.smr-histogram-value { font-size: 11px; font-weight: 600; color: #374151; position: absolute; top: -20px; }' +
'.smr-histogram-label { font-size: 10px; color: #6b7280; text-align: center; margin-top: 8px; line-height: 1.2; position: absolute; bottom: -30px; width: 100%; }' +
'.smr-chart-bar-row { display: flex; align-items: center; margin-bottom: 8px; gap: 8px; }' +
'.smr-chart-bar-label { flex: 0 0 140px; font-size: 12px; color: #4b5563; }' +
'.smr-chart-bar-track { flex: 1; height: 12px; border-radius: 999px; background: #f3f4f6; overflow: hidden; }' +
'.smr-chart-bar { height: 100%; border-radius: 999px; background: #6a8ec9; transition: width 0.3s ease; }' +
'.smr-chart-bar-value { flex: 0 0 32px; font-size: 12px; color: #374151; text-align: right; font-weight: 500; }' +
/\* Scatter plot styles \*/
'.smr-scatter-container { background: #ffffff; border: 1px solid #e5e7eb; border-radius: 12px; padding: 20px; overflow: hidden; max-width: 600px; margin: 24px auto 0; }' +
'.smr-scatter-title { font-size: 16px; font-weight: 600; color: #111827; margin-bottom: 16px; text-align: center; }' +
'.smr-scatter-plot { position: relative; width: 100%; height: 400px; }' +
'.smr-scatter-svg { width: 100%; height: 100%; }' +
'.smr-scatter-point { fill: #6a8ec9; stroke: #ffffff; stroke-width: 1; cursor: pointer; transition: all 0.2s ease; }' +
'.smr-scatter-point:hover { fill: #5677a9; r: 6; stroke-width: 2; }' +
'.smr-scatter-axis { stroke: #d1d5db; stroke-width: 1; }' +
'.smr-scatter-axis-label { font-size: 11px; fill: #6b7280; text-anchor: middle; }' +
'.smr-scatter-axis-title { font-size: 12px; fill: #374151; font-weight: 500; text-anchor: middle; }' +
'.smr-scatter-grid { stroke: #f3f4f6; stroke-width: 1; }' +
'.smr-tooltip { position: absolute; background: rgba(0, 0, 0, 0.8); color: white; padding: 8px 10px; border-radius: 4px; font-size: 11px; pointer-events: none; white-space: nowrap; z-index: 1000; opacity: 0; transition: opacity 0.2s ease; }' +
'.smr-tooltip.visible { opacity: 1; }' +
'@media (max-width: 768px) {' +
'.smr-container { flex-direction: column; }' +
// Off-canvas sidebar styles for mobile - SLIDES FROM RIGHT
'.smr-sidebar { ' +
'position: fixed; ' +
'top: 0; ' +
'right: 0; ' +
'width: 280px; ' +
'height: 100vh; ' +
'z-index: 999; ' +
'transform: translateX(100%); ' +
'transition: transform 0.3s ease; ' +
'border-left: 1px solid #e5e7eb; ' +
'border-right: none; ' +
'overflow-y: auto; ' +
'}' +
'.smr-sidebar.active { transform: translateX(0); }' +
'.smr-sidebar.hidden { transform: translateX(100%); display: flex; }' +
// Show Close button only on mobile
'.smr-close-sidebar-btn { display: block; }' +
'.smr-results-grid { grid-template-columns: 1fr; }' +
'.smr-mobile-filter-toggle { display: block; }' +
'.smr-search-section-desktop { display: none; }' +
'.smr-search-section-mobile { display: block; }' +
'.smr-active-filters-wrapper { align-items: flex-start; }' +
'.smr-tabs-wrapper { padding: 0 16px; }' +
'.smr-tab { padding: 12px 16px; font-size: 14px; }' +
'.smr-about-content { padding: 32px 16px; }' +
'.smr-main-content { padding: 8px 12px; }' +
'.smr-detail-view { padding: 20px 12px; }' +
'.smr-search-section { margin-bottom: 12px; }' +
'.smr-summary-content { padding: 16px; }' +
'.smr-summary-left { position: static; width: auto; padding: 16px 16px 8px; text-align: left !important; margin: 0 !important; display: block; }' +
'.smr-summary-stat { margin-bottom: 12px; padding: 12px; }' +
'.smr-chart-container { max-width: none; margin: 0 auto; }' +
'.smr-histogram-container { max-width: none; margin: 0 auto; }' +
'.smr-histogram-tab { font-size: 12px; padding: 12px 16px; }' +
'.smr-histogram-chart { height: 150px; gap: 4px; padding: 25px 0 35px 0; }' +
'.smr-histogram-label { font-size: 9px; }' +
'.smr-histogram-value { font-size: 10px; }' +
'.smr-chart-tab { font-size: 12px; padding: 12px 16px; }' +
'.smr-scatter-container { max-width: none; margin-top: 16px; }' +
'.smr-scatter-plot { height: 350px; }' +
'}' +
// Intermediate breakpoint for tablets - ensures chart scales nicely between desktop and mobile
'@media (max-width: 1024px) and (min-width: 769px) {' +
'.smr-chart-container { max-width: calc(100vw - 400px); min-width: 500px; }' +
'.smr-histogram-container { max-width: calc(100vw - 400px); min-width: 500px; }' +
'.smr-histogram-chart { height: 180px; padding: 28px 0 38px 0; }' +
'}' +
// Hide Close button on desktop
'@media (min-width: 769px) {' +
'.smr-close-sidebar-btn { display: none; }' +
'}' +
'/\* Divider + right-side layout for About and Designs summary \*/' +
'#smrAboutContent { position: relative; }' +
'.smr-about-left { position: absolute; top: 0; left: 0; width: 280px; padding: 48px 32px; text-align: right; font-weight: 800; font-size: 16px; line-height: 1.3; color: #111827; }' +
'.smr-about-right { padding-left: calc(280px + 32px); padding-top: 48px; }' +
'.smr-about-right p { font-size: 16px; line-height: 1.6; color: #374151; }' +
'@media (max-width: 768px) { .smr-about-left { position: static; width: auto; padding: 16px 16px 8px; text-align: left !important; margin: 0 !important; display: block; } .smr-about-right { padding: 0 16px 16px; } }' +
'#smrAboutContent { min-height: 100vh; }' +
'.smr-about-content { margin: 0; padding-left: 0; }' +
'.smr-tab-content { position: relative; }' +
'#smrSummaryContent { padding-top: 48px; min-height: 100vh; padding-left: calc(280px + 32px); }' +
'#smrAboutContent::before, #smrSummaryContent::before { content: ""; position: absolute; top: 0; bottom: 0; left: 280px; width: 0; border-right: 1px solid #e5e7eb; pointer-events: none; }' +
'@media (max-width: 768px) { #smrAboutContent, #smrSummaryContent { padding-left: 0; } #smrAboutContent::before, #smrSummaryContent::before { content: none; } }' +
'.smr-about-title { font-weight: 800; font-size: 22px; line-height: 1.3; margin: 0 0 12px 0; color: #111827; }' +
'.smr-about-content p { font-size: 16px; line-height: 1.6; color: #374151; }' +
'/\* Compare table overrides to neutralize CMS heading styles \*/#smr-app-container .smr-compare-table thead th { color:#111827 !important; font-weight:700; background:#ffffff; text-transform:none;}#smr-app-container .smr-compare-table tbody td { font-size:13px; color:#6c757d;}#smr-app-container .smr-compare-table tbody td:first-child { color:#374151; font-weight:600;}@media (max-width: 768px){#smr-app-container }/\* Normalize top spacing across all sizes \*/#smr-app-container .smr-container{align-items:flex-start !important;}#smr-app-container .smr-main-content{padding-top:48px !important;margin-top:0 !important;}#smr-app-container .smr-results-header{margin-top:0 !important;padding-top:0 !important;}</style>' +
// Sidebar overlay for mobile
'<div class="smr-sidebar-overlay" id="smrSidebarOverlay"></div>' +
'<div class="smr-tabs-wrapper">' +
'<div class="smr-tabs">' +
'<button class="smr-tab" id="smrAboutTab">About</button>' +
'<button class="smr-tab active" id="smrDatabaseTab">Database</button>' +
'<button class="smr-tab" id="smrSummaryTab">Summary</button>' +
'</div>' +
'</div>' +
'<div class="smr-tab-content" id="smrAboutContent">' +
'<div class="smr-about-left">SMR Design Database</div>' +
'<div class="smr-about-right"><p style="margin:0 0 1rem;">The SMR Design Database provides a comprehensive record of the many small modular reactor (SMR) designs at various stages of development across the world.</p><p style="margin:0 0 1rem;">Users can search for designs, developers, countries, or other technical parameters, and filter results as required. Users can chose to select specific reactors to compare specifications and intended applications.</p><p style="margin:0;">Detailed information is available for each reactor design and links are provided to relevant World Nuclear News articles.</p><p style="margin:1rem 0 0;">For information about SMR projects, please visit our <a href="https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors/small-modular-reactor-smr-global-tracker">SMR Global Project Tracker</a>. The Tracker provides a comprehensive and interactive overview of SMR projects under development worldwide. It includes more than 70 projects at various stages of progress, from initial site preparation through to operation, as well as over 50 key pre-project agreements and related developments.</p></div>' +
'</div>' +
'<div class="smr-tab-content active" id="smrDatabaseContent">' +
'<div class="smr-container">' +
'<aside class="smr-sidebar" id="smrSidebar">' +
// NEW: Sticky header with Close and Reset All buttons
'<div class="smr-sidebar-header">' +
'<div class="smr-sidebar-header-buttons">' +
'<button class="smr-close-sidebar-btn" id="smrCloseSidebarBtn">Close</button>' +
'<button class="smr-reset-all-btn" id="smrResetAllBtn">Reset All</button>' +
'</div>' +
'</div>' +
// Scrollable content area
'<div class="smr-sidebar-content">' +
'<div class="smr-search-section smr-search-section-desktop">' +
'<input type="text" id="smrSearchInput" class="smr-search-box" placeholder="Search">' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="reactorTypeToggle">' +
'<span>Reactor Type</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrReactorTypeFilter" class="smr-checkbox-group" style="display:none;"></div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="countryToggle">' +
'<span>Country</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrCountryFilter" class="smr-checkbox-group" style="display:none;"></div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="smrDesignStatusToggle">' +
'<span>Design Status</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrDesignStatusFilter" class="smr-checkbox-group" style="display:none;"></div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="fuelEnrichmentToggle">' +
'<span>Fuel Enrichment</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrFuelEnrichmentFilter" class="smr-checkbox-group" style="display:none;"></div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="spectrumToggle">' +
'<span>Spectrum</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrSpectrumFilter" class="smr-checkbox-group" style="display:none;"></div>' +
'</div>' +
// NEW: Applications filter
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="applicationsToggle">' +
'<span>Applications</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrApplicationsFilter" class="smr-checkbox-group" style="display:none;"></div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="outletTempToggle">' +
'<span>Outlet Temp (°C)</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrOutletTempFilter" style="display:none;">' +
'<div class="smr-range-inputs">' +
'<div class="smr-range-input-wrapper">' +
'<label>Min</label>' +
'<input type="number" id="smrOutletTempMin" step="1">' +
'</div>' +
'<div class="smr-range-input-wrapper">' +
'<label>Max</label>' +
'<input type="number" id="smrOutletTempMax" step="1">' +
'</div>' +
'</div>' +
'</div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="thermalToggle">' +
'<span>Thermal Capacity (MWt)</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrThermalFilter" style="display:none;">' +
'<div class="smr-range-inputs">' +
'<div class="smr-range-input-wrapper">' +
'<label>Min</label>' +
'<input type="number" id="smrThermalMin" step="1">' +
'</div>' +
'<div class="smr-range-input-wrapper">' +
'<label>Max</label>' +
'<input type="number" id="smrThermalMax" step="1">' +
'</div>' +
'</div>' +
'</div>' +
'</div>' +
'<div class="smr-filter-section">' +
'<div class="smr-filter-toggle" id="grossToggle">' +
'<span>Gross Capacity (MWe)</span>' +
'<span class="smr-arrow">▼</span>' +
'</div>' +
'<div id="smrGrossFilter" style="display:none;">' +
'<div class="smr-range-inputs">' +
'<div class="smr-range-input-wrapper">' +
'<label>Min</label>' +
'<input type="number" id="smrGrossMin" step="1">' +
'</div>' +
'<div class="smr-range-input-wrapper">' +
'<label>Max</label>' +
'<input type="number" id="smrGrossMax" step="1">' +
'</div>' +
'</div>' +
'</div>' +
'</div>' +
'</div>' +
'</aside>' +
'<main class="smr-main-content" id="smrMainContent">' +
'<div class="smr-search-section smr-search-section-mobile" id="smrMobileSearchSection">' +
'<input type="text" id="smrSearchInputMobile" class="smr-search-box" placeholder="Search">' +
'</div>' +
'<button class="smr-mobile-filter-toggle" id="smrMobileFilterToggle">Show Filters</button>' +
'<div class="smr-results-header" style="margin-bottom:8px !important;display:flex !important;justify-content:space-between !important;align-items:center !important;">' +
'<div id="smrResultsCount" class="smr-results-count" style="font-size:14px !important;color:#6c757d !important;margin:0 !important;padding:0 !important;"></div>' +
'<div id="smrSortContainer"></div>' +
'</div>' +
'<div id="smrActiveFiltersWrapper" class="smr-active-filters-wrapper">' +
'<div id="smrFilterChips" class="smr-filter-chips-container"></div>' +
'<button id="smrClearFiltersBtn" class="smr-active-clear-btn">Clear all filters</button>' +
'</div>' +
'<div id="smrCompareBar" class="smr-compare-bar">' +'<strong>Compare:</strong>' +'<div id="smrCompareList" class="smr-compare-list"></div>' +'<button id="smrCompareBtn" class="smr-compare-btn" disabled>Compare</button>' +'</div>' +
'<div id="smrResultsGrid" class="smr-results-grid"></div>' +
'<div id="smrDetailView" class="smr-detail-view"></div>' +
'<div id="smrCompareView" class="smr-detail-view"></div>' +
'</main>' +
'</div>' +
'</div>' +
'<div class="smr-tab-content" id="smrSummaryContent">' +
'<div class="smr-summary-left">' +
'<div class="smr-summary-stat">' +
'<div class="smr-stat-number" id="smrStatDesignsNumber">0</div>' +
'<div class="smr-stat-label">designs</div>' +
'</div>' +
'<div class="smr-summary-stat">' +
'<div class="smr-stat-number" id="smrStatDevelopersNumber">0</div>' +
'<div class="smr-stat-label">developers</div>' +
'</div>' +
'<div class="smr-summary-stat">' +
'<div class="smr-stat-number" id="smrStatCountriesNumber">0</div>' +
'<div class="smr-stat-label">countries</div>' +
'</div>' +
'</div>' +
'<div class="smr-summary-content">' +
'<div class="smr-chart-area-title">Designs by country, type, status and enrichment</div>' +
'<div class="smr-chart-container">' +
'<div class="smr-chart-tabs">' +
'<button class="smr-chart-tab active" data-chart="country">Country</button>' +
'<button class="smr-chart-tab" data-chart="type">Reactor Type</button>' +
'<button class="smr-chart-tab" data-chart="status">Design Status</button>' +
'<button class="smr-chart-tab" data-chart="fuel">Fuel Enrichment</button>' +
'</div>' +
'<div class="smr-chart-content">' +
'<div id="smrChart"></div>' +
'</div>' +
'</div>' +
'<div class="smr-histogram-area-title">Designs by power and outlet temperature</div>' +
'<div class="smr-histogram-container">' +
'<div class="smr-histogram-tabs">' +
'<button class="smr-histogram-tab active" data-histogram="power">Power Output</button>' +
'<button class="smr-histogram-tab" data-histogram="temperature">Outlet Temperature</button>' +
'</div>' +
'<div class="smr-histogram-content">' +
'<div id="smrHistogramChart"></div>' +
'</div>' +
'</div>' +
'</div>' +
'</div>' +
'</div>';
setTimeout(function() {
var scrollPosition = 0;
var aboutTab = document.getElementById('smrAboutTab');
var databaseTab = document.getElementById('smrDatabaseTab');
var summaryTab = document.getElementById('smrSummaryTab');
var aboutContent = document.getElementById('smrAboutContent');
var databaseContent = document.getElementById('smrDatabaseContent');
var summaryContent = document.getElementById('smrSummaryContent');
// ---- Tabs ----
function setActiveTab(tab) {
[aboutTab, databaseTab, summaryTab].forEach(function(t) {
if (t) t.classList.remove('active');
});
[aboutContent, databaseContent, summaryContent].forEach(function(c) {
if (c) c.classList.remove('active');
});
if (tab === 'about') {
if (aboutTab) aboutTab.classList.add('active');
if (aboutContent) aboutContent.classList.add('active');
} else if (tab === 'database') {
if (databaseTab) databaseTab.classList.add('active');
if (databaseContent) databaseContent.classList.add('active');
} else if (tab === 'summary') {
if (summaryTab) summaryTab.classList.add('active');
if (summaryContent) summaryContent.classList.add('active');
renderSummaryCharts();
}
}
if (aboutTab) {
aboutTab.addEventListener('click', function() {
setActiveTab('about');
});
}
if (databaseTab) {
databaseTab.addEventListener('click', function() {
setActiveTab('database');
});
}
if (summaryTab) {
summaryTab.addEventListener('click', function() {
setActiveTab('summary');
});
}
// ---- Existing database/filter logic (unchanged) ----
var sortContainer = document.getElementById('smrSortContainer');
if (sortContainer) {
var wrapper = document.createElement('div');
wrapper.setAttribute('style', 'display:flex;align-items:center;gap:8px;');
var label = document.createElement('span');
label.textContent = 'Sort by:';
label.setAttribute('style', 'font-size:14px;color:#6b7280;font-weight:500;');
var select = document.createElement('select');
select.id = 'smrSortSelect';
select.setAttribute('style', 'appearance:none;-webkit-appearance:none;-moz-appearance:none;padding:8px 32px 8px 12px;border:1px solid #d1d5db;border-radius:6px;font-size:14px;background-color:white;background-image:url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' width=\'16\' height=\'16\' viewBox=\'0 0 16 16\'%3E%3Cpath fill=\'%23666\' d=\'M4 6l4 4 4-4z\'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center;background-size:16px;cursor:pointer;color:#374151;font-family: "Muli", Arial, sans-serif;');
var options = [
{value: 'name', text: 'Name'},
{value: 'country', text: 'Country'},
{value: 'outletTemp', text: 'Outlet Temp'},
{value: 'thermal', text: 'Thermal Capacity'},
{value: 'gross', text: 'Gross Capacity'}
];
options.forEach(function(opt) {
var option = document.createElement('option');
option.value = opt.value;
option.textContent = opt.text;
select.appendChild(option);
});
select.onchange = function() {
window.smrHandleSortChange();
};
wrapper.appendChild(label);
wrapper.appendChild(select);
sortContainer.appendChild(wrapper);
}
var smrContainer = document.querySelector('.smr-container');
var sidebar = document.getElementById('smrSidebar');
var sidebarOverlay = document.getElementById('smrSidebarOverlay');
var mainContent = document.getElementById('smrMainContent');
var resultsHeader = document.querySelector('.smr-results-header');
// Function to close sidebar
function closeSidebar() {
if (sidebar) {
sidebar.classList.remove('active');
}
if (sidebarOverlay) {
sidebarOverlay.classList.remove('active');
}
var mobileFilterToggle = document.getElementById('smrMobileFilterToggle');
if (mobileFilterToggle) {
mobileFilterToggle.textContent = 'Show Filters';
}
document.body.style.overflow = '';
}
// NEW: Close sidebar button handler
var closeSidebarBtn = document.getElementById('smrCloseSidebarBtn');
if (closeSidebarBtn) {
closeSidebarBtn.addEventListener('click', function() {
closeSidebar();
});
}
// NEW: Reset All button handler
var resetAllBtn = document.getElementById('smrResetAllBtn');
if (resetAllBtn) {
resetAllBtn.addEventListener('click', function() {
resetFilters();
// Collapse all filter sections as part of Reset All
(function() {
var pairs = [
['reactorTypeToggle','smrReactorTypeFilter'],
['countryToggle','smrCountryFilter'],
['smrDesignStatusToggle','smrDesignStatusFilter'],
['fuelEnrichmentToggle','smrFuelEnrichmentFilter'],
['spectrumToggle','smrSpectrumFilter'],
['applicationsToggle','smrApplicationsFilter'],
['outletTempToggle','smrOutletTempFilter'],
['thermalToggle','smrThermalFilter'],
['grossToggle','smrGrossFilter']
];
for (var i = 0; i < pairs.length; i++) {
var toggleEl = document.getElementById(pairs[i][0]);
var contentEl = document.getElementById(pairs[i][1]);
if (contentEl) {
contentEl.style.display = 'none';
}
if (toggleEl) {
var arrow = toggleEl.querySelector('.smr-arrow');
if (arrow) arrow.classList.remove('expanded');
// Also update ARIA if present
if (toggleEl.hasAttribute('aria-expanded')) {
toggleEl.setAttribute('aria-expanded', 'false');
}
}
}
})();
// Close sidebar on mobile after resetting
if (window.innerWidth <= 768) {
closeSidebar();
}
});
}
// Mobile filter toggle with off-canvas functionality
var mobileFilterToggle = document.getElementById('smrMobileFilterToggle');
if (mobileFilterToggle) {
mobileFilterToggle.addEventListener('click', function() {
if (!sidebar) return;
if (window.innerWidth <= 768) {
var isActive = sidebar.classList.toggle('active');
if (sidebarOverlay) {
sidebarOverlay.classList.toggle('active', isActive);
}
mobileFilterToggle.textContent = isActive ? 'Hide Filters' : 'Show Filters';
// Prevent body scroll when sidebar is open
if (isActive) {
document.body.style.overflow = 'hidden';
} else {
document.body.style.overflow = '';
}
}
});
}
// Close sidebar when clicking overlay
if (sidebarOverlay) {
sidebarOverlay.addEventListener('click', function() {
closeSidebar();
});
}
// Close sidebar on window resize if switching to desktop
window.addEventListener('resize', function() {
if (window.innerWidth > 768) {
closeSidebar();
}
});
// NEW REACTOR DATA FROM EXCEL
var reactors = [
{
"name": "4S",
"developer": "Toshiba",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 510,
"thermal": 30,
"gross": 10,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "The Super-Safe, Small & Simple (4S) 'nuclear battery' system is being developed by Toshiba and the Central Research Institute of Electric Power Industry (CRIEPI) in Japan in collaboration with SSTAR work and Westinghouse (owned by Toshiba) in the USA. It uses sodium as coolant (with electromagnetic pumps) and has passive safety features, notably negative temperature coefficient of reactivity. The whole unit would be factory-built, transported to site, installed below ground level, and would drive a steam cycle via a secondary sodium loop. It is capable of three decades of continuous operation without refuelling. Metallic fuel (169 pins 10mm diameter) is uranium-zirconium enriched to less than 20% or U-Pu-Zr alloy with 24% Pu for the 30 MWt (10 MWe) version or 11.5% Pu for the 135 MWt (50 MWe) version. Steady power output over the core lifetime in 30 MWt version is achieved by progressively moving upwards an annular reflector around the slender core (0.68m diameter, 2m high in the small version; 1.2m diameter and 2.5m high in the larger version) at about one millimetre per week. After 14 years a neutron absorber at the centre of the core is removed and the reflector repeats its slow movement up the core for 16 more years. Burn-up will be 34 GWday/t. In the event of power loss the reflector falls to the bottom of the reactor vessel, slowing the reaction, and external air circulation gives decay heat removal. A further safety device is a neutron absorber rod which can drop into the core. After 30 years the fuel would be allowed to cool for a year, then it would be removed and shipped for storage or disposal.\n\nBoth versions of 4S are designed to automatically maintain an outlet coolant temperature of 510-550ºC – suitable for power generation with high temperature electrolytic hydrogen production. Plant cost is projected at US$ 2500/kW and power cost 5-7 cents/kWh for the small unit – very competitive with diesel in many locations. The design has gained considerable support in Alaska and toward the end of 2004 the town of Galena granted initial approval for Toshiba to build a 10 MWe (30 MWt) 4S reactor in that remote location. A pre-application Nuclear Regulatory Commission (NRC) review was under way to 2008 with a view to application for design certification in October 2010, and combined construction and operating licence (COL) application to follow. Its review is now listed as ‘inactive’ by NRC. Its design is sufficiently similar to PRISM – GE's modular 150 MWe liquid metal-cooled inherently-safe reactor which went part-way through the NRC approval process (see section above on PRISM) – for it to have good prospects of licensing. Toshiba planned a worldwide marketing program to sell the units for power generation at remote mines, for extraction of tar sands, desalination plants and for making hydrogen. Eventually it expected sales for hydrogen production to outnumber those for power supply.\n\nThe L-4S is a Pb-Bi cooled version of the 4S design.",
"latitude": 35.658,
"longitude": 139.751,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Toshiba-opens-fast-reactor-research-facility ||| Toshiba opens fast reactor research facility ||| February 2008",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Toshiba-prepares-for-nuclear-growth-worldwide ||| Toshiba prepares for nuclear growth worldwide ||| October 2007",
"newsLink3": ""
},
{
"name": "ABV-6E",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 325,
"thermal": 38,
"gross": 9,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "A smaller Russian PWR unit under development by OKBM Afrikantov is the ABV multipurpose power source. It is readily transported to the site, with rapid assembly and operation for 10-12 years between refuelling, which is carried out offsite at special facilities. There is a range of sizes from 45 MWt (ABV-6M ) down to 18 MWt (ABV-3), giving 4-18 MWe outputs. (The IAEA 2011 write-up of the ABV-6M quotes 14 MWt or 6 MWe in cogeneration mode.) The units are compact, with integral steam generator and natural circulation in the primary circuit. They will be factory-produced and designed as a universal power source for floating nuclear plants – the ABV-6M would require a 3500 tonne barge; the ABV-3, 1600 tonne for twin units. The Volnolom FNPP consists of a pair of reactors (12 MWe in total) mounted on a 97-metre, 8700 tonne barge plus a second barge for reverse osmosis desalination (over 40,000 m3/day of potable water).\n\nThe smallest land-based version has reactor module 13 m long and 8.5 m diameter, with a mass of 600 t. The land-based ABV-6M module is 44 m long, 10 m diameter and with mass of 3000 t. The core is similar to that of the KLT-40 except that enrichment is 16.5% or 19.7% and average burn-up 95 GWd/t. It would initially be fuelled in the factory. The service lifetime is about 40 years.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://www.world-nuclear-news.org/articles/eight-ritm-reactors-currently-under-production ||| Eight RITM reactors currently under production ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Construction-starts-on-Russia-s-next-floating-nucl ||| Construction starts on Russias next floating nuclear power plant ||| May 2022",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Russia-relocates-construction-of-floating-power-pl ||| Russia relocates construction of floating power plant ||| July 2007"
},
{
"name": "ABV-6M",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 325,
"thermal": 38,
"gross": 9,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "A smaller Russian PWR unit under development by OKBM Afrikantov is the ABV multipurpose power source. It is readily transported to the site, with rapid assembly and operation for 10-12 years between refuelling, which is carried out offsite at special facilities. There is a range of sizes from 45 MWt (ABV-6M ) down to 18 MWt (ABV-3), giving 4-18 MWe outputs. (The IAEA 2011 write-up of the ABV-6M quotes 14 MWt or 6 MWe in cogeneration mode.) The units are compact, with integral steam generator and natural circulation in the primary circuit. They will be factory-produced and designed as a universal power source for floating nuclear plants – the ABV-6M would require a 3500 tonne barge; the ABV-3, 1600 tonne for twin units. The Volnolom FNPP consists of a pair of reactors (12 MWe in total) mounted on a 97-metre, 8700 tonne barge plus a second barge for reverse osmosis desalination (over 40,000 m3/day of potable water).\n\nThe smallest land-based version has reactor module 13 m long and 8.5 m diameter, with a mass of 600 t. The land-based ABV-6M module is 44 m long, 10 m diameter and with mass of 3000 t. The core is similar to that of the KLT-40 except that enrichment is 16.5% or 19.7% and average burn-up 95 GWd/t. It would initially be fuelled in the factory. The service lifetime is about 40 years.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Floating-a-nuclear-power-plant-in-Yakutia ||| Floating a nuclear power plant in Yakutia ||| October 2007",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Rosatom-to-help-develop-Yakutia-region ||| Rosatom to help develop Yakutia region ||| February 2009",
"newsLink3": "https://world-nuclear-news.org/Articles/Russia-relocates-construction-of-floating-power-pl ||| Russia relocates construction of floating power plant ||| August 2008"
},
{
"name": "ACP100",
"developer": "CNNC (NPIC)",
"country": "China",
"hqCity": "Beijing",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 320,
"thermal": 385,
"gross": 125,
"fuelEnrichment": "<5%",
"designStatus": "Under construction",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The Nuclear Power Institute of China (NPIC), under China National Nuclear Corporation (CNNC), has designed a multi-purpose small modular reactor, the ACP100 or Linglong One. It has passive safety features, notably decay heat removal, and will be installed underground. Seismic tolerance is 300 Gal. It has 57 fuel assemblies 2.15m tall and integral steam generators (320°C), so that the whole steam supply system is produced and shipped a single reactor module. Its 385 MWt produces about 125 MWe, and power plants comprising two to six of these are envisaged, with 60-year design operating lifetime and 24-month refuelling. Or each module can supply 1000 GJ/hr, giving 12,000 m3/day desalination (with MED). Industrial and district heat uses are also envisaged, as well as floating nuclear power plant (FNPP) applications. Capacity of up to 150 MWe is envisaged. In April 2016 the IAEA presented CNNC with its report from the Generic Reactor Safety Review process.\n\nThe Linglong One Demonstration Project\* at Changjiang on Hainan Island involves a joint venture of three main companies: CNNC as owner and operator; the Nuclear Power Institute of China (NPIC) as the reactor designer; and China Nuclear Power Engineering Group (CNPE) being responsible for plant construction. The preliminary safety analysis report for a single unit demonstration plant was approved in April 2020. In May 2022 pouring of concrete for the reactor's basemat was completed. Cold functional tests were completed in October 2025 and non-nuclear steam supply system tests in December 2025. Commercial operation is expected in the first half of 2026.\n\nCNNC signed a second ACP100 agreement with Hengfeng county, Shangrao city in Jiangxi province, and a third with Ningdu county, Ganzhou city in Jiangxi province in July 2013 for another ACP100 project costing CNY 16 billion. Further inland units are planned in Hunan and possibly Jilin provinces. Export potential is considered to be high, with full IP rights. In 2016 CNPE submitted an expression of interest to the UK government based on its ACP100+ design.\n\n\* Hainan Changjiang Multi-purpose Small Modular Reactor Technical Demonstration Project is the full name.",
"latitude": 30.5728,
"longitude": 104.0668,
"newsLink1": "https://www.world-nuclear-news.org/articles/chinese-smr-completes-non-nuclear-steam-start-up-test ||| Chinese SMR completes non-nuclear steam start up test ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/cold-testing-of-chinese-smr-completed ||| Cold testing of Chinese SMR completed ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/first-main-pump-installed-in-chinese-smr ||| First main pump installed in Chinese SMR ||| April 2025"
},
{
"name": "ACP100S",
"developer": "CNNC",
"country": "China",
"hqCity": "Beijing",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 320,
"thermal": 385,
"gross": 125,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "In October 2015 the Nuclear Power Institute of China (NPIC) signed an agreement with UK-based Lloyd's Register to support the development of a floating nuclear power plant (FNPP) using the ACP100S reactor, a marine version of the ACP100. Following approval as part of the 13th Five-Year Plan for innovative energy technologies, CNNC signed an agreement in July 2016 with China Shipbuilding Industry Corporation (CSIC) to prepare for building its ACP100S demonstration floating nuclear plant.",
"latitude": 39.9042,
"longitude": 116.4074,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Installation-of-containment-starts-at-Chinese-SMR ||| Installation of containment starts at Chinese SMR ||| October 2021",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Kepco-E-C-teams-up-with-shipbuilder-for-floating-r ||| Kepco E&C teams up with shipbuilder for floating reactors ||| October 2020",
"newsLink3": "https://www.world-nuclear-news.org/Articles/CNNC-launches-demonstration-SMR-project ||| CNNC launches demonstration SMR project ||| July 2019"
},
{
"name": "ACPR100",
"developer": "CGN",
"country": "China",
"hqCity": "Shenzhen",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 310,
"thermal": 450,
"gross": 140,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "China General Nuclear Group (CGN) has two small ACPR designs: an ACPR100 and ACPR50S, both with passive cooling for decay heat and 60-year design operating lifetime. Both have standard type fuel assemblies and fuel enriched to <5% with burnable poison giving 30-month refuelling. The ACPR100 is an integral PWR, 450 MWt, 140 MWe, having 69 fuel assemblies. Reactor pressure vessel is 17m high and 4.4 m inside diameter, operating at 310 °C. It is designed as a module in larger plant and would be installed underground. The applications for these are similar to those for the ACP100.\n\nThe offshore ACPR50S is 200 MWt, 60 MWe with 37 fuel assemblies and four external steam generators. Reactor pressure vessel is 7.4m high and 2.5 m inside diameter, operating at 310 °C. It is designed for mounting on a barge as a floating nuclear power plant (FNPP). Following approval as part of the 13th Five-Year Plan for innovative energy technologies, CGN announced the construction start on the first FNPP at Bohai Shipyard in Huludao, southwestern Liaoning province, in November 2016. No further announcements on the project have since been made.",
"latitude": 22.5431,
"longitude": 114.0579,
"newsLink1": "https://www.world-nuclear-news.org/Articles/CGN-starts-construction-of-offshore-reactor ||| CGN starts construction of offshore reactor ||| November 2016",
"newsLink2": "https://www.world-nuclear-news.org/Articles/CGN-to-build-floating-reactor ||| CGN to build floating reactor ||| January 2016",
"newsLink3": ""
},
{
"name": "ACPR50S",
"developer": "CGN",
"country": "China",
"hqCity": "Shenzhen",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 320,
"thermal": 200,
"gross": 60,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "China General Nuclear Group (CGN) has two small ACPR designs: an ACPR100 and ACPR50S, both with passive cooling for decay heat and 60-year design operating lifetime. Both have standard type fuel assemblies and fuel enriched to <5% with burnable poison giving 30-month refuelling. The ACPR100 is an integral PWR, 450 MWt, 140 MWe, having 69 fuel assemblies. Reactor pressure vessel is 17m high and 4.4 m inside diameter, operating at 310 °C. It is designed as a module in larger plant and would be installed underground. The applications for these are similar to those for the ACP100.\n\nThe offshore ACPR50S is 200 MWt, 60 MWe with 37 fuel assemblies and four external steam generators. Reactor pressure vessel is 7.4m high and 2.5 m inside diameter, operating at 310 °C. It is designed for mounting on a barge as a floating nuclear power plant (FNPP). Following approval as part of the 13th Five-Year Plan for innovative energy technologies, CGN announced the construction start on the first FNPP at Bohai Shipyard in Huludao, southwestern Liaoning province, in November 2016. No further announcements on the project have since been made.",
"latitude": 22.5431,
"longitude": 114.0579,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Kepco-E-C-teams-up-with-shipbuilder-for-floating-r ||| Kepco E&C teams up with shipbuilder for floating reactors ||| October 2020",
"newsLink2": "https://www.world-nuclear-news.org/Articles/CGN-starts-construction-of-offshore-reactor ||| CGN starts construction of offshore reactor ||| November 2016",
"newsLink3": "https://www.world-nuclear-news.org/Articles/CGN-to-build-floating-reactor ||| CGN to build floating reactor ||| January 2016"
},
{
"name": "A-HTR-100",
"developer": "Eskom",
"country": "South Africa",
"hqCity": "Johannesburg",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 1200,
"thermal": 100,
"gross": 35,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": -26.035,
"longitude": 28.079,
"newsLink1": "https://www.world-nuclear-news.org/articles/stratek-global-and-groupe-albatros-sign-strategic-partnership ||| Stratek Global and Groupe Albatros sign strategic partnership ||| March 2025",
"newsLink2": "https://world-nuclear-news.org/Articles/Partnership-aims-to-drive-forward%C2%A0HTMR-100-SMR-in ||| Partnership aims to drive forward HTMR-100 SMR in South Africa ||| April 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/HTMR-100-team-aim-for-PBMR-SMR-in-South-Africa ||| HTMR-100 team aim for pebble bed SMR in South Africa ||| June 2023"
},
{
"name": "AHWR-300 LEU",
"developer": "BARC",
"country": "India",
"hqCity": "Mumbai",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 285,
"thermal": 920,
"gross": 300,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "The Advanced Heavy Water Reactor developed by the Bhaba Atomic Research Centre (BARC) is designed to make extensive use of India’s abundant thorium as fuel, but a low-enriched uranium fuelled version is pitched for export. This will use low-enriched uranium plus thorium as a fuel, largely dispensing with the plutonium input of the version for domestic use. About 39% of the power will come from thorium (via in situ conversion to U-233, cf two-thirds in domestic AHWR), and burn-up will be 64 GWd/t. Uranium enrichment level will be 19.75%, giving 4.21% average fissile content of the U-Th fuel. It will have vertical pressure tubes in which the light water coolant under high pressure will boil, circulation being by convection. Nominal 300 MWe, 284 MWe net. It is at the basic design stage.",
"latitude": 19.004,
"longitude": 72.911,
"newsLink1": "https://www.world-nuclear-news.org/articles/indias-prototype-fast-breeder-reactor-facing-first-of-a-kind-delay ||| PFBR's first-of-a-kind issues 'being solved systematically' ||| August 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/indian-regulator-approves-fbr-fuel-loading ||| Indian regulator approves FBR fuel loading ||| August 2024",
"newsLink3": "https://www.world-nuclear-news.org/articles/fuel-loading-begins-at-indian-fast-breeder-reactor ||| Fuel loading begins at Indian fast breeder reactor ||| March 2024"
},
{
"name": "AMR",
"developer": "STL Nuclear ",
"country": "South Africa",
"hqCity": "Pretoria",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 10,
"gross": 3,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": -25.6771717526025,
"longitude": 28.271552123286188,
"newsLink1": "https://www.world-nuclear-news.org/articles/uk-seeking-pipeline-of-advanced-nuclear-projects ||| UK seeking pipeline of advanced nuclear projects ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Jacobs-to-assist-in-development-of-UK-Japanese-HTG ||| Jacobs to assist in development of UK-Japanese HTGR ||| May 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/UK-s-NNL-and-Japan-s-JAEA-sign-HTGR-fuel-agreement ||| UK's NNL and Japan's JAEA strengthen HTGR fuel collaboration ||| April 2024"
},
{
"name": "Antares – SC-HTGR",
"developer": "AREVA",
"country": "France",
"hqCity": "Paris",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 850,
"thermal": 600,
"gross": 285,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Another full-size HTR design is being put forward by Framatome (formerly Areva). It is based on the GT-MHR and has also involved Fuji. The reference design is 625 MWt with prismatic block fuel like the GT-MHR. Core outlet temperature is 750°C for the steam-cycle HTR version (SC-HTGR), though an eventual very high temperature reactor (VHTR) version is envisaged with 1000°C and direct cycle. The present concept uses an indirect cycle, with steam in the secondary system, or possibly a helium-nitrogen mix for the VHTR, removing the possibility of contaminating the generation, chemical or hydrogen production plant with radionuclides from the reactor core. It was selected in 2012 for the US Next Generation Nuclear Plant, with two-loop secondary steam cycle, the 625 MWt probably giving 285 MWe per unit, but the primary focus being the 750°C helium outlet temperature for industrial application. It remains at the conceptual design stage.",
"latitude": 48.892,
"longitude": 2.241,
"newsLink1": "https://www.world-nuclear-news.org/Articles/DoE-funds-further-HTGR-studies ||| DoE funds further HTGR studies ||| January 2013",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Areva-modular-reactor-selected-for-NGNP-developmen ||| Areva modular reactor selected for NGNP development ||| February 2012",
"newsLink3": ""
},
{
"name": "AP300",
"developer": "Westinghouse",
"country": "USA",
"hqCity": "Cranberry Township",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 325,
"thermal": 990,
"gross": 330,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 40.685,
"longitude": -80.107,
"newsLink1": "https://www.world-nuclear-news.org/articles/westinghouse-tetra-tech-to-collaborate-on-nuclear-new-build-projects ||| Westinghouse, Tetra Tech to collaborate on nuclear new-build projects ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/westinghouse-expands-uk-supply-chain-for-new-reactors ||| Westinghouse expands UK supply chain for new reactors ||| September 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/ap300-named-as-pick-for-data-centre-deployment ||| Data4 and Westinghouse to evaluate AP300 for data centre deployment ||| March 2025"
},
{
"name": "ARC-100",
"developer": "ARC Clean Technology",
"country": "Canada",
"hqCity": "Saint John",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 510,
"thermal": 286,
"gross": 100,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Advanced Reactor Concepts LLC (ARC) set up in 2006 has developed a 260 MWt/100 MWe sodium-cooled fast reactor based on the 62.5 MWt Experimental Breeder Reactor II (EBR-II). It will be factory-produced, with components readily assembled onsite, and with 'walk-away' passive safety. Installation would be below ground level.\n\nThe ARC-100 system comprises a uranium alloy metal core cartridge submerged in sodium at ambient pressure in a stainless steel tank. The liquid sodium is pumped through the core where it is heated to 510°C, then passed through an integral heat exchanger (within the pool) where it heats sodium in an intermediate loop, which in turn heats working fluid for electricity generation. It would have a refuelling interval of 20 years for cartridge changeover, with 20.7 tonnes of fuel. Initial fuel will be low-enriched uranium (10.1% inner zone, 12.1% middle zone, 17.2% outer zone among 92 fuel assemblies over 1.5 m fuelled height) but it will be able to burn wastes from light water reactors, or plutonium. Reprocessing its used fuel will not separate plutonium. ARC-100 has load-following capability. Thermal efficiency is about 40% and it and could be paired with a supercritical carbon dioxide tertiary circuit to drive a turbine at high efficiency. Operating cost is expected to be $50/MWh.\n\nIn March 2017 GEH and ARC signed an agreement to collaborate on licensing an SMR design based on ARC-100, which will leverage extensive intellectual property and licensing experience of the GEH PRISM programme. A further agreement in August 2017 licensed PRISM technology to ARC, and provided GEH engineering and design expertise to ARC. Initial deployment is envisaged in Canada by ARC Canada, and in October 2019 the CNSC completed phase 1 pre-licensing vendor design review for the ARC-100. Phase 2 was completed in July 2025.\n\nIn July 2018 ARC and New Brunswick Power (NB Power) announced that they were exploring the potential deployment of the ARC-100 reactor at New Brunswick's Point Lepreau nuclear plant, and in November 2020 the two companies were joined by Moltex in setting up an SMR vendor cluster there. In February 2021 the New Brunswick government announced $20 million funding for ARC Canada and in April 2021 plans for the first unit at Point Lepreau were confirmed. In 2021 ARC offered the design to Energoatom in Ukraine. In July 2023 NB Power and ARC Canada submitted an environmental impact assessment registration document and an application for a site preparation licence for an advanced SMR at the Point Lepreau site.",
"latitude": 45.273,
"longitude": -66.063,
"newsLink1": "https://www.world-nuclear-news.org/articles/arc-100-completes-canadian-regulatory-design-review ||| ARC-100 completes Canadian regulatory design review ||| July 2025",
"newsLink2": "https://world-nuclear-news.org/Articles/Partnership-for-ARC-100-commercialisation ||| Partnership for ARC-100 commercialisation ||| May 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/ARC-SMR-proposed-for-green-energy-hub-at-Canadian ||| ARC SMR proposed for green energy hub at Canadian port ||| November 2022"
},
{
"name": "Aurora Powerhouse",
"developer": "Oklo",
"country": "USA",
"hqCity": "Santa Clara",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 500,
"thermal": 205,
"gross": 75,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "Oklo aims to build its first Aurora Powerhouse reactor at Idaho National Laboratory for which the DOE has issued a site use permit. In March 2025, Oklo announced that it had increased the capacity of the Aurora reactor 'platform' from 50 MWe to 75 MWe, offering a flexible output range of 15-75 MWe. The sodium-cooled fast neutron reactor would use high-assay low-enriched U-Zr metallic fuel.\n\nOklo states that the design \"is informed by a robust foundation of prior US Department of Energy (DOE) demonstrations and operational experience with fast reactor technologies, most notably the Experimental Breeder Reactor-II (EBR-II) and the Fast Flux Test Facility (FFTF).\"\n\nOklo was given the go-ahead to begin site characterization work at INL in November 2024 for its first Aurora unit, and in September 2025 held a groundbreaking ceremony. Earlier, in August 2025 Oklo announced that Kiewit Nuclear Solutions Co will serve as lead constructor supporting the design, procurement, and construction of the Aurora Powerhouse.\n\nOklo previously submitted a combined construction and operating licence (COL) application to the NRC in March 2020 to build and operate a 1.5 MWe Aurora fast heatpipe reactor at the INL site. However, the NRC denied this COL application in January 2022.",
"latitude": 37.354,
"longitude": -121.955,
"newsLink1": "https://www.world-nuclear-news.org/articles/oklo-and-siemens-energy-sign-power-conversion-system-contract ||| Oklo and Siemens Energy sign power conversion system contract ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/oklo-fuel-facility-receives-design-approval ||| Oklo fuel facility receives design approval ||| November 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/oklo-breaks-ground-for-first-aurora-powerhouse ||| Oklo breaks ground for first Aurora powerhouse ||| September 2025"
},
{
"name": "BANDI-60",
"developer": "KEPCO E&C",
"country": "South Korea",
"hqCity": "Gimcheon",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 322,
"thermal": 200,
"gross": 60,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The BANDI-60S is a two-loop PWR being developed since 2016 by South Korea’s Kepco Engineering & Construction company. It is a 200 MWt/60 MWe reactor designed for niche markets, particularly floating nuclear power plants. It is described as ‘block type’ with the external steam generators connected directly nozzle-to-nozzle. Initially the steam generators are conventional U-tube, but Kepco is working on a plate and shell design which will greatly reduce their size. Apart from steam generators, most main components including control rod drives are within the pressure vessel. Primary pumps are canned motor, and decay heat removal is passive. There are 52 conventional fuel assemblies, giving 35 GWd/t burn-up with 48-60 month fuel cycle. Burnable absorbers are used instead of soluble boron. Design operating lifetime is 60 years. The pressure vessel is 11.2 m high and 2.8 m diameter. In September 2020 Kepco signed an agreement with Daewoo Shipbuilding & Engineering to develop offshore nuclear power plants using the reactor. ",
"latitude": 36.121,
"longitude": 128.119,
"newsLink1": "https://www.world-nuclear-news.org/articles/abs-approves-korean-smr-power-barge-design ||| ABS approves Korean SMR power barge design ||| October 2023",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Kepco-E-C-teams-up-with-shipbuilder-for-floating-r ||| Kepco E&C teams up with shipbuilder for floating reactors ||| October 2020",
"newsLink3": "https://www.world-nuclear-news.org/Articles/ABS-approves-Korean-SMR-power-barge-design ||| ABS approves Korean SMR power barge design ||| October 2023"
},
{
"name": "Blossom Energy SMR",
"developer": "Blossom Energy",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": null,
"thermal": 180,
"gross": null,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 35.6821372610079,
"longitude": 139.74959516579696,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Blue Capsule",
"developer": "Blue Capsule Technology",
"country": "France",
"hqCity": "Aix-en-Provence",
"reactorType": "Metal-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 150,
"gross": 50,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 43.4914154552854,
"longitude": 5.330792834251141,
"newsLink1": "https://www.world-nuclear-news.org/articles/framatome-plans-french-triso-fuel-pilot-plant ||| Framatome plans French TRISO fuel pilot plant ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/heating-smr-to-be-assessed-for-cadarache-site ||| Heating SMR to be assessed for Cadarache site ||| August 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/smr-developers-enlist-french-nuclear-expertise ||| SMR developers enlist French nuclear expertise ||| May 2024"
},
{
"name": "BREST-OD-300",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 535,
"thermal": 700,
"gross": 300,
"fuelEnrichment": "5-20%",
"designStatus": "Under construction",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Russia has experimented with several lead-cooled reactor designs, and gained 70 reactor-years experience with lead-bismuth cooling to 1990s in submarine reactors. A significant new Russian design from NIKIET is the BREST fast neutron reactor, of 700 MWt, 300 MWe, with lead as the primary coolant, at 540°C, supplying supercritical steam generators. The core sits in a pool of lead at near atmospheric pressure. It is inherently safe and uses a U+Pu nitride fuel. Effective enrichment is about 13.5%. Fuel cycle is quoted at 5-6 years with partial refuelling at about 10 months. No weapons-grade plutonium can be produced (since there is no uranium blanket), and used fuel can be recycled indefinitely, with on-site facilities.\n\nThe pilot demonstration unit is being built at Seversk, with the reactor approximately 70% assembled as of early 2025 and physical launch targeted for 2026, followed by grid connection in the first half of 2027. 1200 MWe units are planned. The BREST reactor is an integral part of the Pilot Demonstration Energy Complex (PDEC) which comprises three elements: a mixed uranium-plutonium nitride fuel fabrication/re-fabrication module, which began pilot operation in January 2025; a nuclear power plant with BREST-300 reactor; and a used nuclear fuel reprocessing module (now expected around 2030). The combination enables a fully closed fuel cycle on one site.",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "https://www.world-nuclear-news.org/articles/fourth-shell-of-brest-od-300-peripheral-cavity-installed ||| Fourth shell of BREST-OD-300 peripheral cavity installed ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/in-pictures-construction-landmarks-for-brest-od-300 ||| In pictures: Construction landmarks for BREST-OD-300 ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/key-equipment-manufactured-for-brest-od-300-reactor ||| Key equipment manufactured for BREST-OD-300 reactor ||| August 2025"
},
{
"name": "BWRX-300",
"developer": "GE Hitachi",
"country": "USA",
"hqCity": "Wilmington",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 288,
"thermal": 870,
"gross": 300,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "GE Hitachi Nuclear Energy has a 300 MWe small BWR design, envisaged as single units. GEH has announced this as the BWRX-300 “which further simplifies the NRC-licensed ESBWR” from which it is derived. The BWRX-300 incorporates a range of cost-saving features, including natural circulation systems, smaller, dry containment, and more passive operational control systems. The estimated capital cost is $2250/kWe for series production after initial units are built. The design aims to limit onsite operational staff numbers to 75 employees to achieve an estimated O&M cost of $16/MWh. In May 2018 the US utility Dominion Energy agreed to help fund the project.\n\nIn July 2018 GEH announced $1.9 million in funding from the US Department of Energy to lead a team including Bechtel, Exelon, Hitachi-GE Nuclear Energy and the Massachusetts Institute of Technology to examine ways to simplify the reactor design, reduce plant construction costs, and lower operation and maintenance costs for the BWRX-300. In particular the team aims to identify ways to reduce plant completion costs by 40-60% compared with other SMR designs in development and to be competitive with gas. \"As the tenth evolution of the boiling water reactor, the BWRX-300 represents the simplest, yet most innovative BWR design since GE began developing nuclear reactors in 1955.\" In May 2021 GEH said that if the design was selected by Ontario Power Generation it planned to bring the BWRX-300 to commercial readiness in partnership with OPG, and that it would be manufactured and constructed in Ontario, with the first unit built at Darlington. In October 2021 GEH engaged BWXT Canada for detailed engineering and design.\n\nIn May 2019 the BWRX-300 was submitted to Canada’s CNSC for a pre-licensing vendor design review. Phase 2 of this commenced in January 2020. After initiating discussion with the US Nuclear Regulatory Commission early in 2019, in January 2020 GE Hitachi announced it had submitted the first licensing topical report for the BWRX-300 SMR to the NRC, using the Part 50 two-step approach and leveraging the ESBWR design certification. GEH expects to have the first unit operating in the USA or Canada about 2028.\nIn October 2019 GEH signed an agreement with Estonia’s Fermi Energia and another agreement with Synthos SA in Poland to examine the economic feasibility of constructing a single BWRX-300 reactor in each country. In December 2020 Exelon in the USA completed a feasibility study for Synthos on deploying the BWRX-300. In June 2021 petrochemical company PKN Orlen joined Synthos in assessing the possibilities.\n\nIn December 2021 OPG announced it had selected GE Hitachi's BWRX-300 SMR for deployment at Darlington. In November 2022 Ontario Power Generation submitted a construction licence application for a BWRX-300 at the Darlington site. The site was licensed in October 2022 for site preparation works. The CNSC issued a construction licence in April 2025, and in May 2025 Ontario authorized construction at an estimated cost of CAD 6.1 billion, with site excavation 87% complete by that time. In January 2023 OPG, GE Hitachi, SNC-Lavalin and Aecon announced a six-year alliance to develop, engineer and construct a BWRX-300 at OPG's Darlington New Nuclear Project. In July 2023 the Ontario government announced it is working with OPG to begin planning and licensing for three additional BWRX-300 units at the Darlington plant site.\n\nIn March 2023 GE Hitachi Nuclear Energy awarded BWXT a reactor pressure vessel engineering contract for its BWRX-300, which involves engineering analysis, design support, manufacturing, and procurement support. In January 2025 BWXT received a contract to manufacture the reactor pressure vessel. In the USA, the Tennessee Valley Authority submitted a construction permit application to the NRC for a BWRX-300 at the Clinch River site in 2025. In the UK, the BWRX-300 completed Step 2 of the generic design assessment in December 2025. In Poland, plans expanded to 24 reactors across six sites.",
"latitude": 34.21,
"longitude": -77.882,
"newsLink1": "https://www.world-nuclear-news.org/articles/bwrx-300-to-be-considered-for-deployment-in-bulgaria ||| BWRX-300 to be considered for deployment in Bulgaria ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/ge-vernova-hitachi-smr-design-cleared-for-use-in-uk ||| GE Vernova Hitachi SMR design clears key UK regulatory stage ||| December 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/gvh-samsung-ct-form-bwrx-300-strategic-alliance ||| GVH, Samsung C&T form BWRX-300 strategic alliance ||| October 2025"
},
{
"name": "CAL-30",
"developer": "Calogena",
"country": "France",
"hqCity": "Paris",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 110,
"thermal": 30,
"gross": 0,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 48.8566,
"longitude": 2.3522,
"newsLink1": "https://www.world-nuclear-news.org/articles/heating-smr-to-be-assessed-for-cadarache-site ||| Heating SMR to be assessed for Cadarache site ||| August 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/first-smr-projects-selected-by-european-industrial-alliance ||| First SMR projects selected by European Industrial Alliance ||| October 2024",
"newsLink3": "https://www.world-nuclear-news.org/articles/french-regulatory-review-of-newcleo-smr-progresses ||| French regulatory review of Newcleo SMR progresses ||| July 2024"
},
{
"name": "CAP150",
"developer": "SNERDI",
"country": "China",
"hqCity": "Shanghai",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 310,
"thermal": 450,
"gross": 150,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "CAP200 or LandStar-V multiple application SMR is a PWR, with SNPTC provenance, being developed from the CAP1000 in parallel with the CAP1400 by SNERDI, using proven fuel and core design. It is 660 MWt/220 MWe and has two external steam generators (301°C). It is pitched to replace coal plants and supply process heat and district heating, with a design operating lifetime of 60 years. With 24-month refuelling, burn-up of 42 GWd/t is expected, the 89 fuel assemblies being the same as those of the CAP1400 but shorter. It has both active and passive cooling, and natural circulation is effective for up to 20% power. In an accident scenario, no operator intervention is required for seven days. It will be installed below grade in a 32 m deep caisson structure, with seismic design basis 600 Gal, even in soft ground. In 2017 the first-of-a-kind cost was estimated at $5000/kW and $160/MWh, dropping to $4000/kW in series.\n\nThe OceanStar-V version would be on a barge, as a floating nuclear power plant.\n\nThe CAP150 is an earlier version, 450 MWt/150 MWe, with eight integral steam generators. It is claimed to have “a more simplified system and more safety than current third generation reactors.” Seismic design basis is 300 Gal. In mid-2013 SNPTC quoted approximately $5000/kW capital cost and 9 c/kWh, so significantly more than the CAP1400.\n\nA related SNERDI project is the CAP50 reactor for floating nuclear power plants. This is to be 200 MWt and relatively low-temperature (250°C), so only about 40 MWe with two external steam generators and five-year refuelling.\n\nSPIC’s LandStar-I is an integral pressure-vessel reactor of 200 MWt with convection circulation at 9 MPa producing hot water for district heating. At SPIC’s Jiamusi demonstration project in Heilongjiang province, two 200 MW LS-I reactors are being built. ",
"latitude": 31.2304,
"longitude": 121.4737,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "CAP200 / LandStar-V",
"developer": "SNERDI",
"country": "China",
"hqCity": "Shanghai",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 313,
"thermal": 660,
"gross": 200,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "CAP200 or LandStar-V multiple application SMR is a PWR, with SNPTC provenance, being developed from the CAP1000 in parallel with the CAP1400 by SNERDI, using proven fuel and core design. It is 660 MWt/220 MWe and has two external steam generators (301°C). It is pitched to replace coal plants and supply process heat and district heating, with a design operating lifetime of 60 years. With 24-month refuelling, burn-up of 42 GWd/t is expected, the 89 fuel assemblies being the same as those of the CAP1400 but shorter. It has both active and passive cooling, and natural circulation is effective for up to 20% power. In an accident scenario, no operator intervention is required for seven days. It will be installed below grade in a 32 m deep caisson structure, with seismic design basis 600 Gal, even in soft ground. In 2017 the first-of-a-kind cost was estimated at $5000/kW and $160/MWh, dropping to $4000/kW in series.\n\nThe OceanStar-V version would be on a barge, as a floating nuclear power plant.\n\nThe CAP150 is an earlier version, 450 MWt/150 MWe, with eight integral steam generators. It is claimed to have “a more simplified system and more safety than current third generation reactors.” Seismic design basis is 300 Gal. In mid-2013 SNPTC quoted approximately $5000/kW capital cost and 9 c/kWh, so significantly more than the CAP1400.\n\nA related SNERDI project is the CAP50 reactor for floating nuclear power plants. This is to be 200 MWt and relatively low-temperature (250°C), so only about 40 MWe with two external steam generators and five-year refuelling.\n\nSPIC’s LandStar-I is an integral pressure-vessel reactor of 200 MWt with convection circulation at 9 MPa producing hot water for district heating. At SPIC’s Jiamusi demonstration project in Heilongjiang province, two 200 MW LS-I reactors are being built. ",
"latitude": 31.2304,
"longitude": 121.4737,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "CAP50",
"developer": "SNERDI",
"country": "China",
"hqCity": "Shanghai",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 250,
"thermal": 200,
"gross": 40,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "CAP200 or LandStar-V multiple application SMR is a PWR, with SNPTC provenance, being developed from the CAP1000 in parallel with the CAP1400 by SNERDI, using proven fuel and core design. It is 660 MWt/220 MWe and has two external steam generators (301°C). It is pitched to replace coal plants and supply process heat and district heating, with a design operating lifetime of 60 years. With 24-month refuelling, burn-up of 42 GWd/t is expected, the 89 fuel assemblies being the same as those of the CAP1400 but shorter. It has both active and passive cooling, and natural circulation is effective for up to 20% power. In an accident scenario, no operator intervention is required for seven days. It will be installed below grade in a 32 m deep caisson structure, with seismic design basis 600 Gal, even in soft ground. In 2017 the first-of-a-kind cost was estimated at $5000/kW and $160/MWh, dropping to $4000/kW in series.\n\nThe OceanStar-V version would be on a barge, as a floating nuclear power plant.\nThe CAP150 is an earlier version, 450 MWt/150 MWe, with eight integral steam generators. It is claimed to have “a more simplified system and more safety than current third generation reactors.” Seismic design basis is 300 Gal. In mid-2013 SNPTC quoted approximately $5000/kW capital cost and 9 c/kWh, so significantly more than the CAP1400.\n\nA related SNERDI project is the CAP50 reactor for floating nuclear power plants. This is to be 200 MWt and relatively low-temperature (250°C), so only about 40 MWe with two external steam generators and five-year refuelling.\n\nSPIC’s LandStar-I is an integral pressure-vessel reactor of 200 MWt with convection circulation at 9 MPa producing hot water for district heating. At SPIC’s Jiamusi demonstration project in Heilongjiang province, two 200 MW LS-I reactors are being built. ",
"latitude": 31.2304,
"longitude": 121.4737,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "CAREM25",
"developer": "CNEA",
"country": "Argentina",
"hqCity": "Buenos Aires",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 326,
"thermal": 100,
"gross": 32,
"fuelEnrichment": "<5%",
"designStatus": "Under construction",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "The CAREM25 reactor prototype being built by the Argentine National Atomic Energy Commission (CNEA), with considerable input from INVAPg, is an older design modular 100 MWt (27 MWe gross) integral pressurized water reactor, first announced in 1984. It has 12 steam generators within the pressure vessel and is designed to be used for electricity generation or as a research reactor or for water desalination (with 8 MWe in cogeneration configuration). CAREM has its entire primary coolant system within the reactor pressure vessel (11m high, 3.5m diameter), self-pressurized and relying entirely on convection (for modules less than 150 MWe). The final full-sized export version will be 100 MWe or more, with axial coolant pumps driven electrically. Fuel is standard 3.1 or 3.4% enriched PWR fuel in hexagonal fuel assemblies, with burnable poison, and is refuelled annually.\n\nThe 25 MWe prototype unit is being built next to Atucha, on the Parana River in Lima, 110 km northwest of Buenos Aires, and the first larger version (probably 100 MWe) is planned in the northern Formosa province, 500 km north of Buenos Aries, once the design is proven. Some 70% of CAREM25 components will be local manufacture. The pressure vessel is being manufactured by Industrias Metalurgicas Pescarmona SA (IMPSA).\n\nThe IAEA lists it as a research reactor under construction since April 2013, though first concrete was poured in February 2014. Construction was halted in May 2024 due to budget cuts, with the project approximately 85% complete. It was originally due online in 2019.\n\nIn March 2015 Argentina’s INVAP and state-owned Saudi technology innovation company Taqnia set up a joint venture company, Invania, to develop nuclear technology for Saudi Arabia's nuclear power programme, apparently focused on CAREM for desalination.",
"latitude": -34.553,
"longitude": -58.464,
"newsLink1": "https://www.world-nuclear-news.org/articles/argentina-sets-out-smr-and-uranium-plans ||| Argentina aiming for SMR and uranium developments ||| June 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/critical-design-review-for-argentina-s-carem-small ||| Argentina's CAREM SMR project to have Critical Design Review ||| May 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Argentina-s-SMR-CNEA-and-Nucleoelectrica-sign-agre ||| CNEA and Nucleoelectrica sign CAREM SMR agreement ||| October 2023"
},
{
"name": "CMSR",
"developer": "Saltfloss Energy",
"country": "Denmark",
"hqCity": "Copenhagen",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 250,
"gross": 100,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "Saltfloss Energy in Denmark (founded 2015, formerly Seaborg Technologies) has a thermal-epithermal single fluid reactor design for a 50 MWt pilot unit Compact Molten Salt Reactor (CMSR) with a view to 250 MWt commercial modular units fuelled by spent LWR fuel and thorium. Fuel salt is Li-7 fluoride initially with uranium as fluoride. Later, thorium, plutonium and minor actinides as fluorides are envisaged as fuel, hence the reactor being called a waste burner. This is pumped through the graphite column core and heat exchanger. Fission products are extracted online. Secondary coolant salt is FLiNaK, at 700°C. Spent LWR fuel would have the uranium extracted for recycle, leaving plutonium and minor actinides to become part of the MSR fuel, with thorium. The company claims very fast power ramp time. High temperature output will allow application to hydrogen production, synthetic fuels, etc.\n\nIn March 2017 the public funding agency Innovation Fund Denmark made a grant to Seaborg to \"build up central elements in its long-term strategy and position itself for additional investments required to progress towards commercial maturity.\" This is the first Danish investment into nuclear fission research since the country introduced a ban on nuclear power in 1985. In December 2020 the American Bureau of Shipping (ABS) issued a feasibility statement regarding the reactor’s use on barges, with 200-800 MWe per barge. This is the first stage in the ABS's five-phase New Technology Qualification process. The company's timeline has been delayed, with deployment now anticipated in the early 2030s. The design has been revised to use LEU fuel with a graphite moderator.",
"latitude": 55.704665623514,
"longitude": 12.553287563046212,
"newsLink1": "https://www.world-nuclear-news.org/articles/denmarks-seaborg-changes-name-and-adds-to-board ||| Denmark's Seaborg changes name and adds to board ||| April 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/seaborg-ready-to-start-licensing-activities-in-south-korea ||| Seaborg 'ready to start licensing activities in South Korea' ||| February 2025",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Seaborg-power-barge-considered-for-use-in-Indonesi ||| Seaborg power barge considered for use in Indonesia ||| September 2023"
},
{
"name": "Copenhagen Atomics Waste Burner",
"developer": "Copenhagen Atomics",
"country": "Denmark",
"hqCity": "Copenhagen",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 100,
"gross": 42,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Copenhagen Atomics is developing the Waste Burner, a 100 MWt thorium molten salt reactor with outlet temperature of 700°C.\n\nThe company describes its reactor core as shaped like an onion (the patented \"Onion Core\"). The outermost layer is a breeding blanket of roughly 2,000 litres of lithium fluoride/thorium fluoride salts at 600°C used to transmute thorium into fissile uranium-233; the next layer is heavy water at 80°C acting as moderator; the next layer is about 200 litres of lithium-6 fluoride/uranium tetrafluoride entering the core at 600°C and exiting at 700°C, serving as both fuel and coolant; and the innermost layer is more heavy water moderator.",
"latitude": 55.6761,
"longitude": 12.5683,
"newsLink1": "https://www.world-nuclear-news.org/articles/copenhagen-atomics-reaches-pump-testing-milestone ||| Copenhagen Atomics reaches pump testing milestone ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/ocean-power-to-consider-deployment-of-danish-smrs ||| Ocean-Power to consider deployment of Danish SMRs ||| July 2025",
"newsLink3": "https://world-nuclear-news.org/articles/copenhagen-atomics-deepgeo-agree-to-collaborate ||| Copenhagen Atomics, DeepGeo agree to collaborate ||| November 2024"
},
{
"name": "DEER",
"developer": "Radiant",
"country": "USA",
"hqCity": "El Segundo",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": null,
"thermal": 3,
"gross": 1,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": true,
"offGrid": true,
"notes": "The DEER (Deployable Electric Energy Reactor) was being developed by Radix Power & Energy Corporation in the USA, in collaboration with Brookhaven Technology Group, Brookhaven National Laboratory, Parsons Corporation, Dunedin Energy Systems, and University of California, Berkeley. The DEER is a PWR and would be portable and sealed, able to operate in the range of 10-50 MWe. DEER-1 was to use fuel based on that in Triga research reactors, with a ten-year cycle, and DEER-2 was to use TRISO fuel, for forward military bases or remote mining sites. No recent information is available.",
"latitude": 33.917,
"longitude": -118.416,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "DF300",
"developer": "Dual Fluid Energy",
"country": "Canada",
"hqCity": "Vancouver",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 1000,
"thermal": 600,
"gross": 300,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 52.52,
"longitude": 13.405,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Demonstration-reactor-to-be-built-in-Rwanda ||| Demonstration reactor to be built in Rwanda ||| September 2023",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Dual-Fluid,-TRIUMF-team-up-for-SMR-development ||| Dual Fluid, TRIUMF team up for SMR development ||| March 2023",
"newsLink3": ""
},
{
"name": "DFBR-1",
"developer": "Deep Fission",
"country": "USA",
"hqCity": "California",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 315,
"thermal": 50,
"gross": 15,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 37.8561913804942,
"longitude": -122.252576120147,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "DHR400",
"developer": "CNNC",
"country": "China",
"hqCity": "Beijing",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 98,
"thermal": 400,
"gross": 0,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "CNNC’s DHR-400 or 'Yanlong' is a 400 MWt pool-type reactor designed for district heating. ",
"latitude": 39.9042,
"longitude": 116.4074,
"newsLink1": "https://world-nuclear-news.org/Articles/Initial-phase-of-Qinshan-district-heating-project ||| Initial phase of Qinshan district heating project commissioned ||| December 2021",
"newsLink2": "https://www.world-nuclear-news.org/Articles/China-confident-of-new-era-for-nuclear-says-CNNC ||| China confident of 'new era' for nuclear, says CNNC president ||| October 2019",
"newsLink3": "https://www.world-nuclear-news.org/Articles/CNNC-completes-design-of-district-heating-reactor ||| CNNC completes design of district heating reactor ||| September 2018"
},
{
"name": "ELENA",
"developer": "Kurchatov Institute",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 328,
"thermal": 3.3,
"gross": 0.7,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 55.807,
"longitude": 37.517,
"newsLink1": "https://world-nuclear-news.org/Articles/Rosatom-plans-new-nuclear-technology-exports ||| Rosatom 'plans new nuclear technology exports' ||| June 2021",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Elysium MCSFR",
"developer": "Elysium Industries",
"country": "USA",
"hqCity": "New York",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 750,
"thermal": 125,
"gross": 50,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Elysium Industries in the USA and Canada has the Molten Chloride Salt Fast Reactor (MCSFR) design with fuel in the chloride salt. It operates below grade at near atmospheric pressure. Primary fuel salt and secondary salt convey heat to steam generators at 650°C. It is designed to load-follow. A range of sizes from 125 to 3000 MWt (50 MWe to 1200 MWe) are under consideration. Used fuel from light water reactors or depleted uranium with some plutonium can fuel it though in 2020 fuel was shown as PuCl3 with fission products, or 15% HALEU. Selected fission products are removed online. Passive safety includes a freeze plug. It has negative temperature and void coefficients. ",
"latitude": 42.886,
"longitude": -78.878,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "EM2",
"developer": "General Atomics",
"country": "USA",
"hqCity": "San Diego",
"reactorType": "Gas-cooled",
"spectrum": "Fast",
"outletTemp": 850,
"thermal": 500,
"gross": 265,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "In February 2010, General Atomics announced its Energy Multiplier Module (EM2) fast neutron design, superseding its GT-MHR. The EM2 is a 500 MWt, 265 MWe helium-cooled fast-neutron HTR operating at 850°C to achieve 53% net thermal efficiency with a variety of fuels and using the Brayton cycle. It has several passive safety features and in particular the fuel rod cladding is manufactured from GA's proprietary SiGA silicon-carbide composite, a high-tech ceramic matrix composite that can withstand more than twice the temperatures of the metal components used in most reactors. Decay heat removal is entirely passive.\n\nThe EM2 may be fuelled with 20 tonnes of used PWR fuel or depleted uranium, plus 22 tonnes of low-enriched uranium (~12% U-235, HALEU) as starter. Used fuel from this is processed to remove fission products (about 4 tonnes) and the balance is recycled as fuel for subsequent rounds, each time topped up with 4 tonnes of further used PWR fuel. Each refuelling cycle may be as long as 30 years. With repeated recycling the amount of original natural uranium (before use by PWR) used goes up from 0.5% to 50% at about cycle 12. High-level waste is about 4% of that from PWR on open fuel cycle. EM2 would also be suitable for process heat applications. The main pressure vessel can be trucked or railed to the site, and installed below ground level, and the high-speed (gas) turbine generator is also truck-transportable. The company expects a four-unit EM2 plant to be built in 42 months. The means of reprocessing to remove fission products is not specified, except that it is not a wet process. The company applied for the second round of DOE funding in 2013.\n\nThe company anticipates a 12-year development and licensing period, which is in line with the 80 MWt experimental technology demonstration gas-cooled fast reactor (GFR) in the Generation IV programmel. GA has teamed up with Chicago Bridge & Iron, Mitsubishi Heavy Industries, and Idaho National Laboratory to develop the EM2.",
"latitude": 32.874,
"longitude": -117.21,
"newsLink1": "https://www.world-nuclear-news.org/articles/ga-reports-progress-on-nuclear-fuel-digital-twin ||| GA reports progress on nuclear fuel digital twin ||| October 2024",
"newsLink2": "https://www.world-nuclear-news.org/Articles/GA-progresses-with-silicon-carbide-fuel-cladding-d ||| GA progresses with silicon carbide fuel cladding development ||| July 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Framatome-and-GA-team-up-on-fast-modular-reactor ||| Framatome and GA team up on fast modular reactor ||| October 2020"
},
{
"name": "Energy Well",
"developer": "Czech Technical University",
"country": "Czech Republic",
"hqCity": "Prague",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 20,
"gross": 8,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "",
"latitude": 50.0755,
"longitude": 14.4378,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "ENHS",
"developer": "UC Berkeley",
"country": "USA",
"hqCity": "Berkeley",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 550,
"thermal": 125,
"gross": 50,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "concept of 50 MWe being developed by the University of California, Berkeley. The core is at the bottom of a metal-filled module sitting in a large pool of secondary molten metal coolant which also accommodates the eight separate and unconnected steam generators. There is convection circulation of primary coolant within the module and of secondary coolant outside it. Outside the secondary pool the plant is air-cooled. Control rods would need to be adjusted every year or so and load-following would be automatic. The whole reactor sits in a 17 metre deep silo. Fuel is a uranium-zirconium alloy with 13% enrichment (or U-Pu-Zr with 11% Pu) with a 15-20 year life. After this the module is removed, stored on site until the primary lead (or Pb-Bi) coolant solidifies, and it would then be shipped as a self-contained and shielded item. A new fuelled module would be supplied complete with primary coolant. The ENHS is designed for developing countries and is highly proliferation-resistant but is not yet close to commercialization.\n\nThe heatpipe ENHS has the heat removed by liquid-metal heatpipes. Like the SAFE-400 space nuclear reactor core, the HP-ENHS core comprises fuel rods and heatpipes embedded in a solid structure arranged in a hexagonal lattice in a 3:1 ratio. The core is oriented horizontally and has a square rather than cylindrical cross-section for effective heat transfer. The heatpipes extend from the two axial reflectors in which the fission gas plena are embedded and transfer heat to an intermediate coolant that flows by natural circulation. (The SAFE-400 space fission reactor – Safe Affordable Fission Engine – was a 400 kWt heatpipe power system of 100 kWe to power a space vehicle using two Brayton power systems (gas turbines driven directly by the hot gas from the reactor.)",
"latitude": 37.8715,
"longitude": -122.273,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "eVinci",
"developer": "Westinghouse",
"country": "USA",
"hqCity": "Cranberry Township",
"reactorType": "Heat pipe-cooled",
"spectrum": "Thermal",
"outletTemp": 600,
"thermal": 15,
"gross": 5,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "The eVinci microreactor of 1 MWe to 5 MWe, but typically 1.6 MWe in present plans, would be fully factory built and fuelled. As well as power generation, process heat to 600°C would be available. Units would have a 40-year lifetime with three-year refuelling interval. They would be transportable, with setup under 30 days. The units would have 'walk-away' safety due to inherent feedback diminishing the nuclear reaction with excess heat, also effecting load-following. There are multiple fuel options for the eVinci, including uranium in oxide, metallic and silicide form. LANL and INL are researching the fuel. Westinghouse is developing the eVinci through testing, analysis and licensing. A DOE Project-Specific Design Review (PSDR) was approved in June 2025, with testing at Idaho National Laboratory anticipated as early as 2026 and commercial manufacturing targeted from 2029. In March 2020 the US Department of Defense awarded a contract for further development of the design (see Military developments section above), possibly using TRISO fuel, as the defense-eVinci (DeVinci), but $11.9 million DOD funding went only to March 2021. In December 2020 the DOE selected Westinghouse for a cost-share project of $9.3 million over seven years (DOE share $7.4 million) to develop the eVinci microreactor with a view then to having a demonstration unit by 2024.\n\nFrom October 2020 an agreement with Bruce Power in Ontario will assess the potential for off-grid deployment in Canada, where it has been submitted for CNSC pre-licensing vendor design review.\n\nIn March 2022 the Canadian government, through Innovation, Science and Economic Development Canada’s (ISED's) Strategic Innovation Fund, announced investment of C$27.2 million ($21.6 million) in the eVinci reactor.\nIn June 2023 Westinghouse established the eVinci Technologies business unit within the company to streamline all aspects of bringing the microreactor to the market.\n\nWestinghouse opened its eVinci Accelerator Hub manufacturing facility in Etna, Pennsylvania in 2024.",
"latitude": 40.685,
"longitude": -80.107,
"newsLink1": "https://www.world-nuclear-news.org/articles/westinghouse-radiant-to-perform-first-us-microreactor-tests ||| Westinghouse, Radiant to perform first US microreactor tests ||| July 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/approval-of-westinghouse-test-microreactor-progresses ||| Approval of Westinghouse test microreactor progresses ||| June 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/westinghouse-and-mcmaster-university-mou-on-evinci-microreactor ||| Westinghouse and McMaster deepen eVinci collaboration ||| April 2025"
},
{
"name": "FLEX",
"developer": "MoltexFLEX",
"country": "UK",
"hqCity": "Birchwood",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 795,
"thermal": 60,
"gross": 24,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 53.391,
"longitude": -2.596,
"newsLink1": "https://www.world-nuclear-news.org/Articles/MoltexFLEX-publishes-research-on-graphite-interact ||| MoltexFLEX publishes research on graphite interaction with molten salt ||| February 2024",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Tweaks-to-FLEX-design-sees-boost-in-power-output ||| Tweaks to FLEX design sees boost in power output ||| September 2023",
"newsLink3": "https://www.world-nuclear-news.org/Articles/MoltexFLEX-wins-grant-for-graphite-research ||| MoltexFLEX wins grant for graphite research ||| February 2023"
},
{
"name": "Flexblue",
"developer": "Naval Group",
"country": "France",
"hqCity": "Paris",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 318,
"thermal": 530,
"gross": 160,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "This was a conceptual design from DCNS (now Naval Group, state-owned), Areva, EdF and CEA from France. It is designed to be submerged, 60-100 metres deep on the sea bed up to 15 km offshore, and returned to a dry dock for servicing. The reactor, steam generators and turbine-generator would be housed in a submerged 12,000 tonne cylindrical hull about 100 metres long and 12-15 metres diameter. Each hull and power plant would be transportable using a purpose-built vessel. Reactor capacity ranged 50-250 MWe, derived from DCNS's latest naval designs, but with details not announced. In 2011 DCNS said it could start building a prototype Flexblue unit in 2013 in its shipyard at Cherbourg for launch and deployment in 2016, possibly off Flamanville, but the project has been cancelled.",
"latitude": 48.841,
"longitude": 2.276,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Russian-designs-for-underwater-nuclear-power-plant ||| Russian designs for underwater nuclear power plant in Arctic ||| July 2023",
"newsLink2": "https://world-nuclear-news.org/Articles/Deep-sea-fission ||| Deep sea fission ||| January 2011",
"newsLink3": ""
},
{
"name": "Flibe LFTR",
"developer": "Flibe Energy",
"country": "USA",
"hqCity": "Huntsville",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 600,
"gross": 250,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Flibe Energy in the USA is studying a 40 MW two-fluid graphite-moderated thermal reactor concept based on the 1960s-'70s US molten-salt reactor programme. It uses lithium fluoride/beryllium fluoride (FLiBe) salt as its primary coolant in both circuits. Fuel is uranium-233 bred from thorium in FLiBe blanket salt. Fuel salt circulates through graphite logs. Secondary loop coolant salt is sodium-beryllium fluoride (BeF2-NaF). A 2 MWt pilot plant is envisaged, and eventually 600 MWt/250 MWe commercial plants.",
"latitude": 34.73,
"longitude": -86.586,
"newsLink1": "https://world-nuclear-news.org/articles/us-funding-for-research-into-recycling-used-nuclear-fuel ||| US funding for research into recycling used nuclear fuel ||| February 2026",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "FMR",
"developer": "General Atomics",
"country": "USA",
"hqCity": "San Diego",
"reactorType": "Gas-cooled",
"spectrum": "Fast",
"outletTemp": 800,
"thermal": 100,
"gross": 44,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "General Atomics Electromagnetic Systems Group (GA-EMS) in the USA is collaborating with Framatome Inc. (the US branch of Framatome) to develop a new helium-cooled 50 MWe design, the Fast Modular Reactor (FMR), primarily for electricity using the Brayton cycle at 45% thermal efficiency. The refuelling cycle would be nine years, apparently using GA’s proprietary SiGA silicon-carbide composite fuel cladding, though no information about fuel has been announced. It will be dry-cooled regarding waste heat, with passive safety. It will have fast-response load-following capability of about 20% per minute ramping while maintaining reactor temperature to mitigate thermal cycle fatigue in components. It will be factory-built and assembled onsite. Framatome’s US engineering team will be responsible for designing several critical structures, systems and components for the FMR. A demonstration unit is expected to operate in early 2030s. Operating temperature is expected to be over 700 °C (cf 850 °C for EM2 at higher thermal efficiency).\n\nGA-EMS is separate from General Atomics' Energy Group, which is developing the Energy Multiplier Module (EM2). GE-EMS is best known for the electromagnetic aircraft launch and recovery systems fitted to the latest US aircraft carriers, as well as rail guns and hypervelocity projectiles.",
"latitude": 32.874,
"longitude": -117.21,
"newsLink1": "https://world-nuclear-news.org/Articles/DOE-selects-advanced-reactor-concepts-for-funding ||| DOE selects advanced reactor concepts for funding ||| December 2020",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Framatome-and-GA-team-up-on-fast-modular-reactor ||| Framatome and GA team up on fast modular reactor ||| October 2020",
"newsLink3": "https://world-nuclear-news.org/Articles/GA-Framatome-team-up-on-fuel-channel-development ||| General Atomics, Framatome join for fuel channel work ||| February 2020"
},
{
"name": "FUJI",
"developer": "IThEMS",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 704,
"thermal": 450,
"gross": 200,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "The Fuji MSR is a graphite-moderated design to operate as a near-breeder with ThF4-UF4 fuel salt and FLiBe coolant at 700°C. It can consume plutonium and actinides, and be from 100 to 1000 MWe. It is being being developed internationally by a Japanese, Russian and US consortium: the International Thorium Molten Salt Forum (ITMSF) based in Japan. Several variants have been designed, including a 10 MWe mini Fuji. Thorium Tech Solutions (TTS) had planned to commercialize the Fuji concept and was working with the Halden test reactor in Norway, which permanently closed in 2018. The status of TTS's commercialization plans is unclear.",
"latitude": 35.0035704678951,
"longitude": 135.76437356493238,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Gen4 module",
"developer": "Gen4 Energy",
"country": "USA",
"hqCity": "Denver",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 500,
"thermal": 70,
"gross": 25,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "The Gen4 Module is a 70 MWt/25 MWe lead-bismuth cooled reactor concept using 19.75% enriched uranium nitride fuel, from Gen4 Energy. The reactor was originally conceived as a potassium-cooled self-regulating 'nuclear battery' fuelled by uranium hydridem. However, in 2009, Hyperion Power changed the design to uranium nitride fuel and lead-bismuth cooling to expedite design certification12. This now classes it as a fast neutron reactor, without moderation. The company claims that the ceramic nitride fuel has superior thermal and neutronic properties compared with uranium oxide. Enrichment is 19.75% and operating temperature about 500°C. The lead-bismuth eutectic is 45% Pb, 55% Bi. The unit would be installed below ground level.\n\nThe reactor vessel housing the core and primary heat transfer circuit is about 1.5 metres wide and 2.5 metres high. It is easily portable, sealed and has no moving parts. A secondary cooling circuit transfers heat to an external steam generator. The reactor module is designed to operate for electricity or process heat (or cogeneration) continuously for up to 10 years without refuelling. Another reactor module could then take its place in the overall plant. The old module, with fuel burned down to about 15% enrichment, would be put in dry storage at site to cool for up to two years before being returned to the factory.\n\nIn March 2010, Hyperion (as the company then was) notified the US Nuclear Regulatory Commission that it planned to submit a design certification application in 2012. The company said then that it has many expressions of interest for ordering units. In September 2010, the company signed an agreement with Savannah River Nuclear Solutions to possibly build a demonstration unit at the Department of Energy site there. Hyperion planned to build a prototype by 2015, possibly with uranium oxide fuel if the nitride were not then available. In March 2012 the US DOE signed an agreement with Hyperion regarding constructing a demonstration unit at its Savannah River site in South Carolina.\n\nIn 2014 two papers on nuclear marine propulsion were published arising from a major international industry project led by Lloyd's Register. They describe a preliminary concept design study for a 155,000 dwt Suezmax tanker that is based on a conventional hull form with a 70 MW Gen4 Energy power module for propulsion.\nIn March 2012 Hyperion Power Generation changed its name to Gen4 Energy, and the name of its reactor to Gen4 Module (G4M). It pitched its design for remote sites having smaller power requirements.",
"latitude": 39.7392,
"longitude": -104.9903,
"newsLink1": "https://www.world-nuclear-news.org/Articles/DoE-agrees-partnerships-for-SMR-deployment ||| DoE agrees partnerships for SMR deployment ||| March 2012",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Hyperion-demo-for-Savannah-River ||| Hyperion demo for Savannah River ||| September 2010",
"newsLink3": "https://world-nuclear-news.org/Articles/First-customer-for-Hyperion-reactor ||| First customer for Hyperion reactor ||| August 2008"
},
{
"name": "GTHTR300",
"developer": "JAEA",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 950,
"thermal": 600,
"gross": 200,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 36.471,
"longitude": 140.606,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "GT-MHR",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 850,
"thermal": 600,
"gross": 288,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "(ORNL) in the USA with the Advanced High-Temperature Reactor (AHTR).16 This is a larger reactor using a coated-particle graphite-matrix TRISO fuel like that in the GT-MHR (see above section on the GT-MHR) and with molten fluoride (FLiBe) salt as primary coolant. While similar to the gas-cooled HTR it operates at low pressure (less than 1 atmosphere) and higher temperature, and gives better heat transfer than helium. The FLiBe salt is used solely as primary coolant, and achieves temperatures of 750-1000°C or more while at low pressure. This could be used in thermochemical hydrogen manufacture.\n\nA small version of the AHTR/FHR is the SmAHTR, with 125 MWt thermal size matched to early process heat markets, or producing 50+ MWe. Operating temperature is 700°C with FLiBe primary coolant and three integral heat exchangers. It is truck transportable, being 9m long and 3.5m diameter. Fuel is 19.75% enriched uranium in TRISO particles in graphite blocks or fuel plates. Refuelling interval is 2.5 to 4 years depending on fuel configuration. Secondary coolant is FLiNaK to Brayton cycle, and for passive decay heat removal, separate auxiliary loops go to air-cooled radiators. Later versions are intended to reach 850-1000°C, using materials yet to be developed.\nReactor sizes of 1500 MWe/3600 MWt are envisaged, with capital costs estimated at less than $1000/kW.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Framatome-and-GA-team-up-on-fast-modular-reactor ||| Framatome and GA team up on fast modular reactor ||| October 2020",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "HAPPY200",
"developer": "SPIC",
"country": "China",
"hqCity": "Beijing",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 120,
"thermal": 200,
"gross": 0,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 39.9042,
"longitude": 116.4074,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "HECTAR",
"developer": "KAERI",
"country": "Korea",
"hqCity": "Daejeon",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 90,
"gross": 0,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 36.374,
"longitude": 127.377,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Hermes demonstration plant",
"developer": "Kairos Power",
"country": "USA",
"hqCity": "Alameda",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 35,
"gross": 20,
"fuelEnrichment": "5-20%",
"designStatus": "Under construction",
"electricity": false,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "Hermes is a 35 MWt reduced-scale fluoride-salt-cooled high-temperature reactor prototype for Kairos Power’s KP-FHR, using 19.75% enriched TRISO pebbles and passive decay-heat removal. The NRC issued a construction permit in December 2023 and first nuclear concrete was poured in May 2025, with operations targeted for 2027.",
"latitude": 37.78,
"longitude": -122.302,
"newsLink1": "https://www.world-nuclear-news.org/articles/kairos-secures-haleu-for-hermes-first-fuel-load ||| Kairos secures HALEU for Hermes' first fuel load ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/kairos-power-installs-third-test-unit-reactor-vessel ||| Kairos Power installs third test unit reactor vessel ||| July 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/first-concrete-for-us-advanced-reactor ||| First concrete for US advanced reactor ||| May 2025"
},
{
"name": "Hermes 2",
"developer": "Kairos Power",
"country": "USA",
"hqCity": "Alameda",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 125,
"gross": 50,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Hermes 2 is the electricity-producing follow-on to Hermes, re-envisioned as a single commercial-scale KP-FHR reactor delivering up to 50 MWe of clean power to the TVA grid under a power purchase agreement with Google. The NRC issued construction permits in November 2024, making it the first electricity-generating Gen IV plant approved for construction in the United States. First nuclear concrete was poured in May 2025, marking start of constrction.",
"latitude": 37.78,
"longitude": -122.302,
"newsLink1": "https://www.world-nuclear-news.org/articles/first-concrete-for-us-advanced-reactor ||| First concrete for US advanced reactor ||| May 2025",
"newsLink2": "https://world-nuclear-news.org/articles/regulator-oks-hermes-2-construction-permit ||| Hermes 2 construction permits approved by US Nuclear Regulatory Commission ||| November 2024",
"newsLink3": ""
},
{
"name": "HEXANA",
"developer": "HEXANA",
"country": "France",
"hqCity": "Aix-en-Provence",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 530,
"thermal": 400,
"gross": 150,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 43.4818861254575,
"longitude": 5.3897546637696525,
"newsLink1": "https://www.world-nuclear-news.org/articles/hexana-smr-to-be-considered-for-deployment-in-the-netherlands ||| Hexana SMR to be considered for deployment in the Netherlands ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/tractebel-and-hexana-launch-smr-cogeneration-task-force ||| Tractebel and Hexana launch SMR cogeneration task force ||| November 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/norwegian-smr-project-development-firm-launched ||| Norwegian SMR project development firm launched ||| June 2025"
},
{
"name": "Holos Mono",
"developer": "HolosGen",
"country": "USA",
"hqCity": "Virginia",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 855,
"thermal": 22,
"gross": 10,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "HolosGen is designing a 22 MWt micro-modular HTR in collaboration with the US military, to fit into a ISO standard 40 ft (12.2 m) shipping container. It is essentially a closed-loop jet engine (Brayton cycle) with the combustor replaced by a nuclear heat source comprising four subcritical power modules (SPMs) that are actively positioned in relation to one another, eliminating control rod mechanisms and enabling rapid load following from 3 MWe to 13 MWe. Placing the SPMs close together allows sufficient neutron transfer to reach criticality.\n\nIt uses 15% enriched TRISO fuel in graphite hexagonal blocks with 6 mm helium channels and core outlet temperature of 650-850 °C. Burnable poison is in the graphite blocks, not the fuel. Heat exchangers are embedded with the compressor components to recover waste heat for an independent organic Rankine cycle. The turbo-machinery is magnetically levitated to eliminate mechanical couplings and bearings in the core. When set up, the plant is shielded by a prefabricated structure. \n\nCore lifetime relates to mass, and a 15-tonne core can operate for about 3.5 years, while a 27 t one can run for over eight years. \n\nIn June 2018, the HolosGen transportable reactor project was awarded $2.3 million by the Advanced Research Projects Agency-Energy (ARPA-E) of the US Department of Energy (DOE) to demonstrate the viability of the concept. An October 2018 study commissioned by the US Army put the estimated cost of a first-of-a-kind 13 MWe unit at $140 million, reducing to $75 million for later units.\n\nHolosGen is working with Argonne National Laboratory.",
"latitude": 38.303,
"longitude": -77.46,
"newsLink1": "https://www.world-nuclear-news.org/Articles/DOE-announces-funding-for-innovative-nuclear-techn ||| DOE announces funding for innovative nuclear technology ||| June 2018",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Holos Quad",
"developer": "HolosGen",
"country": "USA",
"hqCity": "Virginia",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 850,
"thermal": 22,
"gross": 10,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "HolosGen is designing a 22 MWt micro-modular HTR in collaboration with the US military, to fit into a ISO standard 40 ft (12.2 m) shipping container. It is essentially a closed-loop jet engine (Brayton cycle) with the combustor replaced by a nuclear heat source comprising four subcritical power modules (SPMs) that are actively positioned in relation to one another, eliminating control rod mechanisms and enabling rapid load following from 3 MWe to 13 MWe. Placing the SPMs close together allows sufficient neutron transfer to reach criticality.\n\nIt uses 15% enriched TRISO fuel in graphite hexagonal blocks with 6 mm helium channels and core outlet temperature of 650-850 °C. Burnable poison is in the graphite blocks, not the fuel. Heat exchangers are embedded with the compressor components to recover waste heat for an independent organic Rankine cycle. The turbo-machinery is magnetically levitated to eliminate mechanical couplings and bearings in the core. When set up, the plant is shielded by a prefabricated structure. \n\nCore lifetime relates to mass, and a 15-tonne core can operate for about 3.5 years, while a 27 t one can run for over eight years. \n\nIn June 2018, the HolosGen transportable reactor project was awarded $2.3 million by the Advanced Research Projects Agency-Energy (ARPA-E) of the US Department of Energy (DOE) to demonstrate the viability of the concept. An October 2018 study commissioned by the US Army put the estimated cost of a first-of-a-kind 13 MWe unit at $140 million, reducing to $75 million for later units.\n\nHolosGen is working with Argonne National Laboratory.",
"latitude": 38.303,
"longitude": -77.46,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "HTGR-POLA",
"developer": "NCBJ",
"country": "Poland",
"hqCity": "Otwock-Świerk",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 30,
"gross": 11.5,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 52.105,
"longitude": 21.261,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Conceptual-design-of-Polish-HTGR-released ||| Conceptual design of Polish HTGR released ||| June 2023",
"newsLink2": "https://world-nuclear-news.org/Articles/Japan-and-Poland-to-begin-work-on-high-temperature ||| Japan and Poland to begin work on high-temperature reactor design ||| November 2022",
"newsLink3": "https://world-nuclear-news.org/Articles/Poland-plans-next-stage-of-HTGR-development ||| Poland plans next stage of HTR development ||| May 2021"
},
{
"name": "HTMR100",
"developer": "Stratek Global",
"country": "South Africa",
"hqCity": "Pretoria",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 100,
"gross": 35,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "A further conceptual design is the HTMR-100, a 35 MWe (100 MWt) pebble bed HTR for electricity or process heat. The conceptual design, commenced in 2012, from Steenkampskraal Thorium Limited (STL) in South Africa, was completed in 2018. Also known as the Th-100, it is derived from the Jülich and PBMR designs. For electricity, single units have load-following capability, or four can comprise a 140 MWe power plant. There are a range of fuel options involving LEU, thorium and reactor-grade plutonium, with burn-up of 80-90 GWd/t of TRISO fuel pebbles. It has a graphite moderator and helium coolant at 750°C, and a single pass fuel cycle. The reactor vessel is 15 m high, 5.9 m diameter and primary loop pressure is relatively low at 4 MPa.",
"latitude": -25.7479,
"longitude": 28.2293,
"newsLink1": "https://www.world-nuclear-news.org/articles/stratek-global-and-groupe-albatros-sign-strategic-partnership ||| Stratek Global and Groupe Albatros sign strategic partnership ||| March 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/south-africa-government-reiterates-commitment-to-new-nuclear-and-pbmr ||| South Africa 'committed to new nuclear and PBMR' ||| December 2024",
"newsLink3": "https://www.world-nuclear-news.org/articles/partnership-aims-to-drive-forward%C2%A0htmr-100-smr-in ||| Partnership aims to drive forward HTMR-100 SMR in South Africa ||| April 2024"
},
{
"name": "HTR50S",
"developer": "JAEA",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 50,
"gross": 17.2,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Japan Atomic Energy Agency's (previously Japan Atomic Energy Research Institute's) High-Temperature Test Reactor (HTTR) of 30 MWt started up at the end of 1998 and first reached full power with a reactor outlet coolant temperature of 850°C in December 2001. In 2004 it achieved 950°C outlet temperature, and in 2009 it ran at 950°C for 50 days. Its fuel is TRISO particles with low-enriched (average 6%) uranium in prisms and its main purpose is to develop a thermochemical means of producing hydrogen from water.\n\nBased on the HTTR, JAERI is developing the Gas Turbine High Temperature Reactor 300 for Cogeneration (GTHTR-300C) of up to 600 MWt per module. It uses improved HTTR fuel elements with 14% enriched uranium achieving high burn-up (120 GWd/t). Helium at 850-950°C drives a horizontal turbine at 47% efficiency to produce up to 300 MWe. The core consists of 90 hexagonal fuel columns 8 metres high arranged in a ring, with reflectors. Each column consists of eight one-metre high elements 0.4 m across and holding 57 fuel pins made up of fuel particles with 0.55 mm diameter kernels and 0.14 mm buffer layer. In each two-yearly refuelling, alternate layers of elements are replaced so that each remains for four years. It is being developed with Mitsubishi Heavy Industries (MHI), Toshiba/IHI and Fuji, and target for commercialization is about 2030. \n\nJAEA's small HTR50S reactor based on the HTTR is a conceptual design for industrial process and heat and/or power generation. This is 50 MWt with dual reactor outlet temperatures of 750°C and 900°C with maximum use of conventional technologies in order to deploy them in developing countries in the 2020s. Initially this would use a steam cycle for power generation, then improve the fuel, and then Increase the reactor outlet temperature to 900°C and install an intermediate heat exchanger (IHX) to demonstrate helium GT and hydrogen production using the IS process. \n\nEarly in 2019 the Japan Atomic Energy Agency (JAEA) formed a joint venture with Penultimate Power UK to build a 10 MWe SMR there based on the HTTR – referred to as the EH HTGR – for power and process heat in industrial clusters. Plans include scaling up the design to 100 MWe and building a factory in the UK for multiple plants. Penultimate Power claims the first reactor will cost about £100 million ($140 million), with reductions for future units. It expects the first reactor to be operating by 2029.",
"latitude": 36.471,
"longitude": 140.606,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "HTR-PM",
"developer": "INET/Tsinghua University",
"country": "China",
"hqCity": "Beijing",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 250,
"gross": 105,
"fuelEnrichment": "5-20%",
"designStatus": "In operation",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Construction of a larger version of the HTR-10, China's HTR-PM, was approved in principle in November 2005, with preparation for first concrete in mid-2011 and full construction start intended in December 2012. It is also based on the German HTR-Modul design of 200 MWt. Originally envisaged as a single 200 MWe (450 MWt) unit, this will now have twin reactors, each of 250 MWt driving a single 210 MWe steam turbine.\*\n\n\* The size was reduced to 250 MWt from earlier 458 MWt modules in order to retain the same core configuration as the prototype HTR-10 and avoid moving to an annular design like South Africa's PBMR (see section on PMBR below)\n\nEach reactor has a single steam generator with 19 elements (665 tubes). The fuel as 60 mm diameter pebbles is 8.5% enriched (520,000 elements in the two reactors) giving 90 GWd/t discharge burn-up. Core outlet temperature is 750ºC for the helium, steam temperature is 566°C and core inlet temperature is 250°C. It has a thermal efficiency of 40%. Core height is 11 metres, diameter 3 m in a 25 m high, 5.7 m diameter reactor vessel. There are two independent reactivity control systems: the primary one consists of 24 control rods in the side graphite reflector, the secondary one of six channels for small absorber spheres falling by gravity, also in the side reflector. Pebbles are released into the top of the core one by one with the reactor operating. They are correspondingly removed from the bottom, broken ones are separated, the burn-up is measured, and spent fuel elements are screened out and transferred to storage. A 40-year operating lifetime is expected.\n\nChina Huaneng Group, one of China's major generators, is the lead organization involved in the demonstration unit with 47.5% share; China Nuclear Engineering & Construction (CNEC) has a 32.5% stake and Tsinghua University's INET 20% – it being the main R&D contributor. Projected cost is $430 million (but later units falling to $1500/kW with generating cost about 5 ¢/kWh). The HTR-PM rationale is both eventually to replace conventional reactor technology for power, and also to provide for future hydrogen production. INET is in charge of R&D, and was aiming to increase the size of the 250 MWt module and also utilize thorium in the fuel.\n\nThe 210 MWe Shidaowan HTR-PM demonstration plant at Rongcheng in Shandong province achieved first criticality in September 2021 and was connected to the grid in December 2021. It began commercial operation in December 2023, having started construction at the end of 2012. It is to pave the way for commercial 600 MWe reactor units (6x250 MWt, total 655 MWe) with a single heat exchanger and turbine, also using the steam cycle at 43.7% thermal efficiency. Plant operating lifetime is envisaged as 40 years with 85% load factor. The capital cost per kW is expected to be 75% of the small HTR-PM, and for subsequent units, 50%. Meanwhile CNEC is promoting the technology for HTR-PM 600 plants using six 250 MWt modules. Eventually a series of HTRs, possibly with Brayton cycle directly driving the gas turbines, would be factory-built and widely installed throughout China.\n\nPerformance of both this and South Africa's PBMR design includes great flexibility in loads (40-100%) without loss of thermal efficiency, and with rapid change in power settings. Power density in the core is about one-tenth of that in a light water reactor, and if coolant circulation ceases the fuel will survive initial high temperatures while the reactor shuts itself down – giving inherent safety. Power control is by varying the coolant pressure, and hence flow. (See also section on Shidaowan HTR-PM in the information page on Nuclear Power in China and the Research and development section in the information page on China's Nuclear Fuel Cycle).",
"latitude": 40.006,
"longitude": 116.326,
"newsLink1": "https://www.world-nuclear-news.org/articles/china-launches-htgr-industrial-alliance ||| China launches HTGR industrial alliance ||| December 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/construction-of-second-shidaowan-hualong-one-begins ||| Construction of second Shidaowan Hualong One begins ||| May 2025",
"newsLink3": "https://www.world-nuclear-news.org/Articles/HTR-PM-heating-project-commissioned ||| HTR-PM heating project commissioned ||| April 2024"
},
{
"name": "HTTR",
"developer": "JAEA",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 850,
"thermal": 30,
"gross": 0,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Japan Atomic Energy Agency's (previously Japan Atomic Energy Research Institute's) High-Temperature Test Reactor (HTTR) of 30 MWt started up at the end of 1998 and first reached full power with a reactor outlet coolant temperature of 850°C in December 2001. In 2004 it achieved 950°C outlet temperature, and in 2009 it ran at 950°C for 50 days. Its fuel is TRISO particles with low-enriched (average 6%) uranium in prisms and its main purpose is to develop a thermochemical means of producing hydrogen from water.\n\nBased on the HTTR, JAERI is developing the Gas Turbine High Temperature Reactor 300 for Cogeneration (GTHTR-300C) of up to 600 MWt per module. It uses improved HTTR fuel elements with 14% enriched uranium achieving high burn-up (120 GWd/t). Helium at 850-950°C drives a horizontal turbine at 47% efficiency to produce up to 300 MWe. The core consists of 90 hexagonal fuel columns 8 metres high arranged in a ring, with reflectors. Each column consists of eight one-metre high elements 0.4 m across and holding 57 fuel pins made up of fuel particles with 0.55 mm diameter kernels and 0.14 mm buffer layer. In each two-yearly refuelling, alternate layers of elements are replaced so that each remains for four years. It is being developed with Mitsubishi Heavy Industries (MHI), Toshiba/IHI and Fuji, and target for commercialization is about 2030. \n\nJAEA's small HTR50S reactor based on the HTTR is a conceptual design for industrial process and heat and/or power generation. This is 50 MWt with dual reactor outlet temperatures of 750°C and 900°C with maximum use of conventional technologies in order to deploy them in developing countries in the 2020s. Initially this would use a steam cycle for power generation, then improve the fuel, and then Increase the reactor outlet temperature to 900°C and install an intermediate heat exchanger (IHX) to demonstrate helium GT and hydrogen production using the IS process.\n\nEarly in 2019 the Japan Atomic Energy Agency (JAEA) formed a joint venture with Penultimate Power UK to build a 10 MWe SMR there based on the HTTR – referred to as the EH HTGR – for power and process heat in industrial clusters. Plans include scaling up the design to 100 MWe and building a factory in the UK for multiple plants. Penultimate Power claims the first reactor will cost about £100 million ($140 million), with reductions for future units. It expects the first reactor to be operating by 2029.",
"latitude": 36.471,
"longitude": 140.606,
"newsLink1": "https://www.world-nuclear-news.org/Articles/MHI-to-lead-development-of-Japanese-HTGR ||| MHI to lead development of Japanese HTGR ||| July 2023",
"newsLink2": "https://www.world-nuclear-news.org/Articles/JAEA,-MHI-team-up-for-HTTR-hydrogen-project ||| JAEA, MHI team up for HTTR hydrogen project ||| April 2022",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Japanese-gas-cooled-reactor-restarts ||| Japanese gas-cooled reactor restarts ||| August 2021"
},
{
"name": "IMSR400",
"developer": "Terrestrial Energy",
"country": "Canada",
"hqCity": "Oakville",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 440,
"gross": 195,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Canada-based Terrestrial Energy set up in 2013 has designed the Integral MSR (IMSR). This simplified MSR integrates the primary reactor components, including primary heat exchangers to secondary clean salt circuit, in a sealed and replaceable core vessel that has a projected life of seven years. The IMSR will operate at 600-700°C, which can support many industrial process heat applications. The moderator is a hexagonal arrangement of graphite elements. The fuel-salt is a eutectic of standard-assay (5%) low-enriched uranium fuel (UF4) and a fluoride carrier salt at atmospheric pressure. Secondary loop coolant salt is ZrF4-KF at atmospheric pressure. Tertiary steam is at 600°C for power generation, process heat, or to back up wind and solar. Emergency cooling and residual heat removal are passive. Each plant would have space for two reactors, allowing a seven-year changeover, with the used unit removed for offsite reprocessing when it has cooled and fission products have decayed. Terrestrial Energy hopes to commission its first commercial reactor in the 2020s.\n\nThe IMSR is scalable but from 2016 the company has been focused on a 440 MWt/195 MWe unit. The total levelized cost of electricity from the largest is projected to be competitive with natural gas. The smallest is designed for off-grid, remote power applications, and as prototype. Industrial heat at 600°C is also envisaged in 2016 plans. In September 2021 the company announced its 390 MWe IMSR400 upgraded power plant with twin reactors and generators.\n\nCompared with other MSR designs, the company deliberately avoids using thorium-based fuels or any form of breeding, due to “their additional technical and regulatory complexities.” In September 2021 the company contracted Orano for full fuel services worldwide for the IMSR and in October it awarded contracts to BWXT Canada for steam supply systems.\n\nIn November 2017 Terrestrial Energy completed phase 1 of the Canadian Nuclear Safety Commission's (CNSC's) pre-licensing vendor design review of the IMSR-400, and in October 2018 it entered phase 2 of the review. Phase 2 was completed in April 2023. \nEarlier, in January 2019 the company notified the US Nuclear Regulatory Commission (NRC) of its intention to seek design approval for the IMSR-400. In December 2019 the CNSC and the US NRC selected Terrestrial Energy's IMSR for the first joint technical review of an advanced, non-light water nuclear reactor. Terrestrial Energy hopes to commission its first commercial reactor in the 2020s. The IMSR is a candidate for the US Advanced Reactor Demonstration Program but did not get a grant for early (seven-year) development.\n\nIn February 2019 the project progressed to stage 2 of site evaluation by Canadian Nuclear Laboratories – a separate process to licensing – in relation to possibly siting a commercial plant at Chalk River by 2026. Since November 2019 IMSR development has been supported by Canadian Nuclear Laboratories' Canadian Nuclear Research Initiative (CNRI). In October 2020 a C$20 million grant from Canada's Strategic Innovation Fund was announced, to accelerate development of the IMSR.\n\nIn January 2015 the company announced a collaborative agreement with US Oak Ridge National Laboratory (ORNL) to advance the design over about two years, and in May a similar agreement with the Dalton Nuclear Institute in the UK. In March 2017 the company entered into a contract with the University of New Brunswick for validation and verification work for the IMSR. In August 2021 the company signed an agreement with Westinghouse in the UK for fuel development and supply. The company has applied for a US loan guarantee of up to $1.2 billion to support financing of a project to license, construct and commission the first US IMSR, a 190 MWe commercial facility. In November 2021 the DOE made a $3 million grant to support licensing and commercialization of the IMSR.\n\nTerrestrial Energy has pivoted its initial US deployment to the RELLIS Campus near Texas A&M University, selected in February 2025. In January 2026 the DOE executed an Other Transaction Authority agreement under Project TETRA to support deployment. The company listed on Nasdaq in October 2025.",
"latitude": 43.467,
"longitude": -79.687,
"newsLink1": "https://www.world-nuclear-news.org/articles/terrestrial-energy-oklo-execute-DOE-agreements ||| Terrestrial Energy, Oklo execute DOE agreements ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/expanded-contract-signed-for-pilot-uk-molten-salt-reactor-fuel-plant ||| Contract signed for pilot UK integral molten salt reactor fuel plant ||| November 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/doe-announces-first-selections-for-pilot-reactor-programme ||| DOE announces first selections for pilot reactor programme ||| August 2025"
},
{
"name": "i-SMR",
"developer": "KAERI",
"country": "South Korea",
"hqCity": "Daejeon",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 321,
"thermal": 520,
"gross": 170,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 36.374,
"longitude": 127.377,
"newsLink1": "https://www.world-nuclear-news.org/articles/korean-smrs-to-be-considered-for-norwegian-project ||| Korean SMRs to be considered for Norwegian project ||| July 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/oklo-khnp-to-cooperate-on-smr-projects ||| Oklo, KHNP to cooperate on SMR projects ||| May 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/korean-city-to-study-feasibility-of-i-smr-deployme ||| Korean city to study feasibility of i-SMR deployment ||| July 2024"
},
{
"name": "JIMMY",
"developer": "Jimmy Energy",
"country": "Czech Republic",
"hqCity": "Prague",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 5,
"gross": 1.5,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 50.0727005662777,
"longitude": 14.432376644716705,
"newsLink1": "https://www.world-nuclear-news.org/articles/heating-smr-to-be-assessed-for-cadarache-site ||| Heating SMR to be assessed for Cadarache site ||| August 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/french-regulatory-review-of-newcleo-smr-progresses ||| French regulatory review of Newcleo SMR progresses ||| July 2024",
"newsLink3": ""
},
{
"name": "KARAT-100",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 286,
"thermal": 360,
"gross": 100,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "A larger version of the KARAT-45 reactor design. ",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "KARAT-45",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 286,
"thermal": 180,
"gross": 45,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "This is a 45 MWe tank-type BWR as a stand-alone cogeneration plant. The design includes natural circulation in its core cooling system for heat removal in all operational modes and incorporates passive safety systems. A larger version is 100 MWe. ",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "KLT-40S",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 316,
"thermal": 150,
"gross": 35,
"fuelEnrichment": "5-20%",
"designStatus": "In operation",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "The first floating nuclear power plant using KLT-40S reactors, the Akademik Lomonosov, commenced construction in 2007, and was grid connected at Pevek in December 2019. (See also Floating nuclear power plants section in the information page on Nuclear Power in Russia.)\n\nDerived from the KLT-40 reactor well proven in icebreakers and now – with low-enriched fuel – on a barge, for remote area power supply. Units are designed to run 3-4 years between refuelling with on-board refuelling capability and used fuel storage. All fuel assemblies are replaced in each such refuelling. At the end of a 12-year operating cycle the whole plant is taken to a central facility for overhaul and storage of used fuel. Operating plant lifetime is 40 years. Two units are mounted on a 21,500 tonne barge. Although the reactor core is normally cooled by forced circulation (four-loop), the design relies on convection for emergency cooling. \n\nA variant of this is the KLT-20, specifically designed for floating nuclear plants. It is a two-loop version with the same enrichment but with a ten-year refuelling interval.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://www.world-nuclear-news.org/articles/russias-floating-nuclear-power-plant-passes-one-billion-kwh ||| Russia's floating nuclear power plant passes one billion kWh ||| January 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/refuelling ||| First refuelling at floating nuclear power plant ||| November 2023",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Floating-nuclear-power-plant-set-for-first-refuell ||| Floating nuclear power plant set for first refuelling ||| October 2023"
},
{
"name": "KP-FHR",
"developer": "Kairos Power",
"country": "USA",
"hqCity": "Alameda",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 320,
"gross": 140,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Kairos Power in the USA has designed a 320 MWt/140 MWe fluoride (FLiBe) salt-cooled high temperature reactor (KP-FHR) which it plans to build at the East Tennessee Technology Park at Oak Ridge, Tennessee, in collaboration with Oak Ridge National Laboratory. The reactor uses 19.75% enriched TRISO fuel in pebble form with online refuelling and operates at up to 650°C. Secondary circuit salt is ‘solar’ nitrate, feeding a steam generator. It has passive shutdown and decay heat removal. The prototype is the Hermes reduced-scale test reactor of 35 MWt, selected by the DOE in December 2020 for a $629 million programme over seven years (DOE share $303 million). In May 2021 the Tennessee Valley Authority (TVA) agreed to provide engineering, operations, and licensing support for the Hermes project. TVA holds an early site permit for the Clinch River site. In October 2021 Kairos submitted its preliminary safety analysis report to the NRC as part of its construction licence application for the $100 million Hermes demonstration unit In November 2024 the NRC issued construction permits for Hermes 2, a two-unit commercial demonstration facility. In October 2024 Google announced a partnership with Kairos Power for up to 500 MW of KP-FHR capacity. With the first deployment targeted by 2030.",
"latitude": 37.78,
"longitude": -122.302,
"newsLink1": "https://www.world-nuclear-news.org/articles/kairos-secures-haleu-for-hermes-first-fuel-load ||| Kairos secures HALEU for Hermes' first fuel load ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/kairos-power-installs-third-test-unit-reactor-vessel ||| Kairos Power installs third test unit reactor vessel ||| July 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/first-concrete-for-us-advanced-reactor ||| First concrete for US advanced reactor ||| May 2025"
},
{
"name": "KRONOS MMR",
"developer": "NANO Nuclear Energy",
"country": "USA",
"hqCity": "New York",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 660,
"thermal": 45,
"gross": 15,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 40.7128,
"longitude": -74.006,
"newsLink1": "https://www.world-nuclear-news.org/articles/nano-progresses-north-american-projects ||| NANO progresses North American projects ||| October 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/nano-to-build-illinois-mmr-facility ||| NANO to build Illinois MMR facility ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/agreement-to-build-microreactor-on-us-university-site ||| Agreement to build microreactor on US university site ||| April 2025"
},
{
"name": "LDR-50",
"developer": "Steady Energy",
"country": "Finland",
"hqCity": "Espoo",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 150,
"thermal": 50,
"gross": 0,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 60.1699,
"longitude": 24.9384,
"newsLink1": "https://www.world-nuclear-news.org/articles/construction-of-steady-energy-pilot-plant-begins ||| Construction of Steady Energy pilot plant begins ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/international-safety-assessments-of-finnish-french-smrs ||| International safety assessments of Finnish, French SMRs ||| January 2026",
"newsLink3": "https://www.world-nuclear-news.org/articles/regulator-completes-preliminary-assessment-steady-energys-smr-concept ||| Regulator completes preliminary assessment of Steady Energy's SMR concept ||| June 2025"
},
{
"name": "Leadir-PS100",
"developer": "Northern Nuclear",
"country": "Canada",
"hqCity": "Cambridge",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 560,
"thermal": 100,
"gross": 36,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": true,
"offGrid": false,
"notes": "This is a new design from Northern Nuclear Industries in Canada, combining a number of features in unique combination. The 100 MWt, 36 MWe reactor has a graphite moderator, TRISO fuel in pebbles, lead (Pb-208) as primary coolant, all as integral pool-type arrangement at near atmospheric pressure. It delivers steam at 370°C, and is also envisaged as an industrial heat plant. The coolant circulates by natural convection. The fuel pebbles are in four cells, each with graphite reflectors, and capacity can be increased by adding cells. Shutdown rods are similar to those in CANDU reactors. Passive decay heat removal is by air convection. The company presents it as a Gen IV design",
"latitude": 43.3966405557932,
"longitude": -80.3208198037476,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "LEUNR",
"developer": "Canadian Space Mining Corporation",
"country": "Canada",
"hqCity": "Toronto",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 130,
"thermal": 0.1,
"gross": 0,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 43.7104437580867,
"longitude": -79.3556313383522,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "LFR-AS-200",
"developer": "newcleo",
"country": "France",
"hqCity": "Paris",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 530,
"thermal": 480,
"gross": 200,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 51.5074,
"longitude": -0.1278,
"newsLink1": "https://www.world-nuclear-news.org/articles/eagles-and-newcleo-team-up-for-lfr-technology-demonstrator ||| Eagles and Newcleo team up for LFR technology demonstrator ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/newcleo-submits-smr-design-for-euratom-safeguards-review ||| Newcleo submits SMR design for Euratom safeguards review ||| December 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/newcleo-to-scale-back-uk-operations ||| Newcleo to scale back UK operations ||| July 2025"
},
{
"name": "LFR-AS-30",
"developer": "newcleo",
"country": "France",
"hqCity": "Paris",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 530,
"thermal": 90,
"gross": 30,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 51.5074,
"longitude": -0.1278,
"newsLink1": "https://www.world-nuclear-news.org/articles/newcleo-offered-site-for-mox-fuel-plant ||| Newcleo offered site for MOX fuel plant ||| July 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/newcleo-plans-fuel-development-centre ||| Newcleo plans fuel development centre ||| March 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/newcleo-seeks-to-buy-land-for-demonstration-smr ||| Newcleo seeks to buy land for demonstration SMR ||| February 2025"
},
{
"name": "LFR-TL-30",
"developer": "newcleo",
"country": "France",
"hqCity": "Paris",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 440,
"thermal": 100,
"gross": 30,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 51.5074,
"longitude": -0.1278,
"newsLink1": "https://www.world-nuclear-news.org/articles/consortium-to-speed-up-development-of-lead-cooled ||| Consortium to speed up development of lead-cooled SMRs ||| November 2023",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Westinghouse,-Ansaldo-progress-with-LFR-developmen ||| Westinghouse, Ansaldo progress with LFR development ||| May 2023",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Westinghouse-and-Ansaldo-Nucleare-collaborate-on-n ||| Westinghouse and Ansaldo Nucleare collaborate on next-gen LFR nuclear plant ||| October 2022"
},
{
"name": "LOKI MMR",
"developer": "NANO Nuclear Energy",
"country": "USA",
"hqCity": "New York",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 727,
"thermal": 5,
"gross": 1.5,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 40.7128,
"longitude": -74.006,
"newsLink1": "https://www.world-nuclear-news.org/articles/agreements-for-potential-deployment-of-nano-microreactors ||| Agreements for potential deployment of NANO microreactors ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/british-firm-to-acquire-odin-microreactor-design ||| British firm to acquire ODIN microreactor design ||| September 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/nano-reactor-core-block-ready-for-testing ||| NANO reactor core block ready for testing ||| March 2025"
},
{
"name": "LSPR",
"developer": "Tokyo Institute of Technology",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 525,
"thermal": 150,
"gross": 53,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": true,
"offGrid": false,
"notes": "A lead-bismuth-eutectic (LBE) cooled fast reactor of 150 MWt/53 MWe, the LSPR (LBE-Cooled Long-Life Safe Simple Small Portable Proliferation-Resistant Reactor), is under development in Japan. Fuelled units would be supplied from a factory and operate for 30 years, then be returned. The concept is intended for developing countries.",
"latitude": 35.604,
"longitude": 139.683,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "MARVEL Research Microreactor",
"developer": "INL/DOE",
"country": "USA",
"hqCity": "Idaho Falls",
"reactorType": "Metal-cooled",
"spectrum": "Thermal",
"outletTemp": 520,
"thermal": 0.1,
"gross": 0.02,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "The DOE plans to build the Microreactor Applications Research Validation and Evaluation (MARVEL) reactor, a 100 kWt microreactor at Idaho. It is designed to perform research and development on various operational features of microreactors to improve their integration with end-user applications and is described in the Research Reactors information page.",
"latitude": 43.492,
"longitude": -112.04,
"newsLink1": "https://www.world-nuclear-news.org/articles/first-projects-selected-for-inl-reactor-experiments ||| First projects selected for INL reactor experiments ||| December 2025",
"newsLink2": "https://www.world-nuclear-news.org/Articles/TRIGA-International-begins-fabricating-MARVEL-fuel ||| TRIGA International begins fabricating MARVEL fuel ||| February 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/US-microreactor-apparatus-begins-tests ||| US microreactor apparatus begins tests ||| September 2023"
},
{
"name": "MHR-100",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 850,
"thermal": 215,
"gross": 50,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "MicroURANUS",
"developer": "MicroURANUS Corp.",
"country": "South Korea",
"hqCity": "Ulsan",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 350,
"thermal": 60,
"gross": 20,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 43.655268210955,
"longitude": -79.3661704412818,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Mini Fuji",
"developer": "IThEMS",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 10,
"gross": 4,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 35.0035704678951,
"longitude": 135.76437356493238,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "MMR-10",
"developer": "Ultra Safe Nuclear Corporation",
"country": "USA",
"hqCity": "Seattle",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 30,
"gross": 10,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "Ultra Safe Nuclear Corporation (USNC), an American company with subsidiaries in Canada and elsewhere, has the Micro Modular Reactor (MMR) HTR with the TRISO fuel in pellets in prismatic graphite blocks in a sealed transportable core. Two versions operate at 15 MWt/5 MWe or 30 MWt/10 MWe with flexible output and they require no refuelling in a 20-year operating lifetime, after which the module becomes waste. Heat is transferred from the core by helium to a molten salt system. Larger versions are envisaged.\n\nPhase 1 of a pre-licensing vendor design review by the Canadian Nuclear Safety Commission (CNSC) was completed in February 2019, and Global First Power (GFP, jointly owned by USNC and Ontario Power Generation, OPG) then submitted a site preparation licence application for Chalk River. CNSC’s environmental assessment began in July 2019. GFP, based in Ottawa, describes itself as an energy provider specializing in project development, licensing, ownership and operation of small nuclear power plants to supply clean power and heat to remote industrial operations and residential settlements. Formal licence review by the CNSC for the 15 MWt MMR began in May 2021.\n\nIn June 2020 a joint venture was formed between USNC and OPG to build, own and operate the proposed MMR project at Chalk River, Ontario. The joint venture – the Global First Power Limited Partnership – is owned equally by OPG and USNC-Power, the Canadian subsidiary of USNC. GFP said it would \"provide project development, licensing, construction and operation\" services for the project. The MMR would provide 15 MWt of process heat via molten salt, and have an operating lifetime of 20 years. \n\nIn August 2020 USNC signed an agreement with Hyundai Engineering and Korea Atomic Energy Research Institute for development and deployment of HTR technology for supplying power as well as process heat.\n\nIn November 2020 USNC signed an agreement with Poland’s Synthos and applied to the Polish government for financing industrial-scale hydrogen projects. \n\nIn June 2021 the University of Illinois announced plans to install a USNC MMR as both a power source and research reactor at its Urbana-Champaign campus. \n\nIn April 2018, Canadian Nuclear Laboratories (CNL) launched its SMR review – a separate process to licensing – with a view to having an SMR constructed on its Chalk River site by 2026. GFP/OPG/USNC completed the first and second stages of CNL's process, and was invited to participate in the third and penultimate stage. Construction of the first 5 MWe demonstration reactor at Chalk River is expected to start in 2023, for 2025 commissioning. This will be followed by one at Idaho National Laboratory and one at the University of Illinois.\n\nIn 2020 USNC proposed an integrated solar, wind and nuclear plant providing 120 MWe of generation and 1 TWh per year for a remote defence base using ten 10 MWe MMR units. Projected power cost is 10 ¢/kWh.\n(USNC is also developing an accident-tolerant shutdown system for NASA in nuclear thermal propulsion systems.)",
"latitude": 47.6062,
"longitude": -122.3321,
"newsLink1": "https://www.world-nuclear-news.org/articles/nano-progresses-north-american-projects ||| NANO progresses North American projects ||| October 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/nano-to-build-illinois-mmr-facility ||| NANO to build Illinois MMR facility ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/british-firm-to-acquire-odin-microreactor-design ||| British firm to acquire ODIN microreactor design ||| September 2025"
},
{
"name": "MMR-5",
"developer": "Ultra Safe Nuclear Corporation",
"country": "USA",
"hqCity": "Seattle",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 15,
"gross": 5,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "Ultra Safe Nuclear Corporation (USNC), an American company with subsidiaries in Canada and elsewhere, has the Micro Modular Reactor (MMR) HTR with the TRISO fuel in pellets in prismatic graphite blocks in a sealed transportable core. Two versions operate at 15 MWt/5 MWe or 30 MWt/10 MWe with flexible output and they require no refuelling in a 20-year operating lifetime, after which the module becomes waste. Heat is transferred from the core by helium to a molten salt system. Larger versions are envisaged.\n\nPhase 1 of a pre-licensing vendor design review by the Canadian Nuclear Safety Commission (CNSC) was completed in February 2019, and Global First Power (GFP, jointly owned by USNC and Ontario Power Generation, OPG) then submitted a site preparation licence application for Chalk River. CNSC’s environmental assessment began in July 2019. GFP, based in Ottawa, describes itself as an energy provider specializing in project development, licensing, ownership and operation of small nuclear power plants to supply clean power and heat to remote industrial operations and residential settlements. Formal licence review by the CNSC for the 15 MWt MMR began in May 2021.\n\nIn June 2020 a joint venture was formed between USNC and OPG to build, own and operate the proposed MMR project at Chalk River, Ontario. The joint venture – the Global First Power Limited Partnership – is owned equally by OPG and USNC-Power, the Canadian subsidiary of USNC. GFP said it would \"provide project development, licensing, construction and operation\" services for the project. The MMR would provide 15 MWt of process heat via molten salt, and have an operating lifetime of 20 years. \n\nIn August 2020 USNC signed an agreement with Hyundai Engineering and Korea Atomic Energy Research Institute for development and deployment of HTR technology for supplying power as well as process heat.\n\nIn November 2020 USNC signed an agreement with Poland’s Synthos and applied to the Polish government for financing industrial-scale hydrogen projects. \n\nIn June 2021 the University of Illinois announced plans to install a USNC MMR as both a power source and research reactor at its Urbana-Champaign campus. \n\nIn April 2018, Canadian Nuclear Laboratories (CNL) launched its SMR review – a separate process to licensing – with a view to having an SMR constructed on its Chalk River site by 2026. GFP/OPG/USNC completed the first and second stages of CNL's process, and was invited to participate in the third and penultimate stage. Construction of the first 5 MWe demonstration reactor at Chalk River is expected to start in 2023, for 2025 commissioning. This will be followed by one at Idaho National Laboratory and one at the University of Illinois.\n\nIn 2020 USNC proposed an integrated solar, wind and nuclear plant providing 120 MWe of generation and 1 TWh per year for a remote defence base using ten 10 MWe MMR units. Projected power cost is 10 ¢/kWh.\n(USNC is also developing an accident-tolerant shutdown system for NASA in nuclear thermal propulsion systems.)",
"latitude": 47.6062,
"longitude": -122.3321,
"newsLink1": "https://www.world-nuclear-news.org/articles/nano-progresses-north-american-projects ||| NANO progresses North American projects ||| October 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/nano-to-build-illinois-mmr-facility ||| NANO to build Illinois MMR facility ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/british-firm-to-acquire-odin-microreactor-design ||| British firm to acquire ODIN microreactor design ||| September 2025"
},
{
"name": "MN-1",
"developer": "MobileNuclear Energy",
"country": "USA",
"hqCity": "Virginia",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 1,
"gross": 0.35,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 37.2312204582167,
"longitude": -78.7132627536418,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Moltex SSR-Th",
"developer": "Moltex Energy",
"country": "United Kingdom",
"hqCity": "London",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 600,
"thermal": null,
"gross": null,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Moltex Energy’s Stable Salt Reactor (SSR) is a conceptual UK MSR reactor design that relies on convection from static vertical fuel tubes in the core to convey heat to the reactor coolant. Because the nuclear material is contained in fuel assemblies, standard industrial pumps can be used for the low radioactivity coolant salt. Core temperature is 500-600°C, at atmospheric pressure. Decay heat is removed by natural air convection.\n\nFuel tubes three-quarters filled with the molten fuel salt are grouped into fuel assemblies which are similar to those used in standard reactors, and use similar structural materials. The fuel salt is about 60% NaCl, 20% PuCl2, 20% UCl3, with almost any level of actinide & lanthanide trichlorides mixed in depending on the spent oxide fuel used in reprocessing – about 16% fissile overall. The individual fuel tubes are vented so that noble fission product gases escape into the coolant salt, which is a ZrF4-KF-NaF mixture, the radionuclide accumulation of which is managed. Iodine and caesium stay dissolved in the fuel salt. Other fission product gases condense on the upper fuel tube walls and fall back into the fuel mixture before they can escape into the coolant. The fuel assemblies can be moved laterally without removing them. Refuelling is thus continuous online, and after the fuel is sufficiently burned up the depleted assemblies are stored at one side of the pool for a month to cool, then lifted out so that the salt freezes. Reprocessing is straightforward, and any level of lanthanides can be handled.\n\nSSR factory-produced modules are 150 MWe containing fuel, pumps, primary heat exchanger, control blades and instrumentation. Several, up to gigawatt-scale, can share a reactor tank, half-filled with the coolant salt which transfers heat away from the fuel assemblies to the peripheral steam generators, essentially by convection, at atmospheric pressure. There are three variants of the SSR: the Stable Salt Reactor – Wasteburner (SSR-W) fast reactor; about two years behind developmentally, the SSR-U thermal-spectrum reactor for a variety of applications; and the SSR-Th with thorium fuel. The GridReserve version has heat storage.\n\nThe SSR-W is the simplest and cheapest, due to compact core and no moderator. The primary fissile fuel in this original fast reactor version was to be plutonium-239 chloride with minor actinides and lanthanides, recovered from LWR fuel or from an SSR-U reactor. In 2020 the SSR-W fuel was 25% reactor-grade PuCl3 with 30% UCl3 and 45% KCl. Primary coolant salt is ZrF4-KF at a maximum temperature of 590°C. Secondary coolant is nitrate salt buffer. Burn-up is 120-200 GWd/t. A 750 MWt/300 MWe demonstration plant is envisaged, the SSR-W300. An agreement has been signed with New Brunswick Power for initial deployment at Point Lepreau in Canada and in March 2021 the Canadian government announced a C$50.5 million investment towards this. In April 2021 plans were confirmed for this plus a plant for recycling used Canadian nuclear fuel for it. In November 2020 the two companies were joined by ARC Canada in setting up an SMR vendor cluster there. The Canadian Nuclear Safety Commission pre-licensing vendor design review of the SSR-W has completed the first phase. The first operating reactor is envisaged after 2030. The UK parent company Moltex Energy entered administration in March 2025. The Canadian subsidiary continues development, and in March 2025 demonstrated its WAste To Stable Salt (WATSS) reprocessing process on actual used CANDU fuel.\n\nThe company has announced the physically larger and more expensive SSR-U ‘global workhorse version’ of its design, with a thermal neutron spectrum running on LEU fluorides (up to 7% enriched) with graphite built into the fuel assemblies, which increases the size of the core. It runs at a higher temperature than the fast version – minimum 600°C – with ZrF4-NaF coolant salt stabilized with ZrF2. As well as electricity, hydrogen production is its purpose. It is designed to be compatible with thorium breeding to U-233. It is seen as having a much larger potential market, and initial deployment in the UK in the 2030s is anticipated, with potential for replacing CCGT and coal plants.\n\nThe SSR-Th is a thorium breeder version of the SSR-U, with thorium in the coolant salt and the U-233 produced is progressively dissolved in bismuth at the bottom of the salt pool. This contains U-238 to denature it and ensure there is never a proliferation risk. Once the desired level of U-233 is achieved (under 20%), the bismuth with uranium is taken out batch-wise, and the mixed-isotope uranium is chlorinated to become fuel. If the fuel is used in a fast reactor, plutonium and actinides can be added.\n\nMoltex has also put forward its GridReserve molten nitrate salt heat storage concept to enable the reactor to supplement intermittent renewables.",
"latitude": 45.273,
"longitude": -66.063,
"newsLink1": "https://www.world-nuclear-news.org/articles/moltex-requests-pre-licensing-consultation-for-recycling-process ||| Moltex requests pre-licensing consultation for recycling process ||| April 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/pivotal-moment-for-moltex-recycling-process ||| Pivotal moment for Moltex recycling process ||| March 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/moltex-reactor-can-consume-used-fuel-research-confirms ||| Moltex reactor can consume used fuel, research confirms ||| October 2024"
},
{
"name": "Moltex SSR-W",
"developer": "Moltex Energy",
"country": "United Kingdom",
"hqCity": "London",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 600,
"thermal": 750,
"gross": 300,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Moltex Energy’s Stable Salt Reactor (SSR) is a conceptual UK MSR reactor design that relies on convection from static vertical fuel tubes in the core to convey heat to the reactor coolant. Because the nuclear material is contained in fuel assemblies, standard industrial pumps can be used for the low radioactivity coolant salt. Core temperature is 500-600°C, at atmospheric pressure. Decay heat is removed by natural air convection.\n\nFuel tubes three-quarters filled with the molten fuel salt are grouped into fuel assemblies which are similar to those used in standard reactors, and use similar structural materials. The fuel salt is about 60% NaCl, 20% PuCl2, 20% UCl3, with almost any level of actinide & lanthanide trichlorides mixed in depending on the spent oxide fuel used in reprocessing – about 16% fissile overall. The individual fuel tubes are vented so that noble fission product gases escape into the coolant salt, which is a ZrF4-KF-NaF mixture, the radionuclide accumulation of which is managed. Iodine and caesium stay dissolved in the fuel salt. Other fission product gases condense on the upper fuel tube walls and fall back into the fuel mixture before they can escape into the coolant. The fuel assemblies can be moved laterally without removing them. Refuelling is thus continuous online, and after the fuel is sufficiently burned up the depleted assemblies are stored at one side of the pool for a month to cool, then lifted out so that the salt freezes. Reprocessing is straightforward, and any level of lanthanides can be handled.\n\nSSR factory-produced modules are 150 MWe containing fuel, pumps, primary heat exchanger, control blades and instrumentation. Several, up to gigawatt-scale, can share a reactor tank, half-filled with the coolant salt which transfers heat away from the fuel assemblies to the peripheral steam generators, essentially by convection, at atmospheric pressure. There are three variants of the SSR: the Stable Salt Reactor – Wasteburner (SSR-W) fast reactor; about two years behind developmentally, the SSR-U thermal-spectrum reactor for a variety of applications; and the SSR-Th with thorium fuel. The GridReserve version has heat storage.\n\nThe SSR-W is the simplest and cheapest, due to compact core and no moderator. The primary fissile fuel in this original fast reactor version was to be plutonium-239 chloride with minor actinides and lanthanides, recovered from LWR fuel or from an SSR-U reactor. In 2020 the SSR-W fuel was 25% reactor-grade PuCl3 with 30% UCl3 and 45% KCl. Primary coolant salt is ZrF4-KF at a maximum temperature of 590°C. Secondary coolant is nitrate salt buffer. Burn-up is 120-200 GWd/t. A 750 MWt/300 MWe demonstration plant is envisaged, the SSR-W300. An agreement has been signed with New Brunswick Power for initial deployment at Point Lepreau in Canada and in March 2021 the Canadian government announced a C$50.5 million investment towards this. In April 2021 plans were confirmed for this plus a plant for recycling used Canadian nuclear fuel for it. In November 2020 the two companies were joined by ARC Canada in setting up an SMR vendor cluster there. The Canadian Nuclear Safety Commission pre-licensing vendor design review of the SSR-W has completed the first phase. The first operating reactor is envisaged after 2030.\n\nThe company has announced the physically larger and more expensive SSR-U ‘global workhorse version’ of its design, with a thermal neutron spectrum running on LEU fluorides (up to 7% enriched) with graphite built into the fuel assemblies, which increases the size of the core. It runs at a higher temperature than the fast version – minimum 600°C – with ZrF4-NaF coolant salt stabilized with ZrF2. As well as electricity, hydrogen production is its purpose. It is designed to be compatible with thorium breeding to U-233. It is seen as having a much larger potential market, and initial deployment in the UK in the 2030s is anticipated, with potential for replacing CCGT and coal plants.\n\nThe SSR-Th is a thorium breeder version of the SSR-U, with thorium in the coolant salt and the U-233 produced is progressively dissolved in bismuth at the bottom of the salt pool. This contains U-238 to denature it and ensure there is never a proliferation risk. Once the desired level of U-233 is achieved (under 20%), the bismuth with uranium is taken out batch-wise, and the mixed-isotope uranium is chlorinated to become fuel. If the fuel is used in a fast reactor, plutonium and actinides can be added.\n\nMoltex has also put forward its GridReserve molten nitrate salt heat storage concept to enable the reactor to supplement intermittent renewables.",
"latitude": 45.273,
"longitude": -66.063,
"newsLink1": "https://www.world-nuclear-news.org/articles/moltex-requests-pre-licensing-consultation-for-recycling-process ||| Moltex requests pre-licensing consultation for recycling process ||| April 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/pivotal-moment-for-moltex-recycling-process ||| Pivotal moment for Moltex recycling process ||| March 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/moltex-reactor-can-consume-used-fuel-research-confirms ||| Moltex reactor can consume used fuel, research confirms ||| October 2024"
},
{
"name": "MoveluX",
"developer": "Toshiba",
"country": "Japan",
"hqCity": "Kawasaki",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 685,
"thermal": 10,
"gross": 3,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 35.658,
"longitude": 139.751,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "mPower",
"developer": "BWXT",
"country": "USA",
"hqCity": "Lynchburg",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 320,
"thermal": 530,
"gross": 195,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "In mid-2009, Babcock & Wilcox (B&W) announced its mPower reactor, a 500 MWt, 180 MWe integral PWR designed to be factory-made and railed to sitei. It was a deliberately conservative design, to more readily gain acceptance and licensing. In November 2012 the US Department of Energy (DOE) announced that it would support accelerated development of the design for early deployment, with up to $226 million, and it paid $111 million of this.\n\nThe reactor pressure vessel containing core of 2x2 metres and steam generator is thus only 3.6 metres diameter and 22 m high, and the whole unit 4.5 m diameter and 23 m high. It would be installed below ground level, have an air-cooled condenser giving 31% thermal efficiencyp, and passive safety systems. The power was originally 125 MWe, but by about 2014, 195 MWe was quoted when water-cooled. A 155 MWe air-cooled version was also planned. The integral steam generator is derived from marine designs, as is the control rod set-up. Convection would be assisted by eight small canned-motor coolant pumps. It has a \"conventional core and standard fuel\" (69 fuel assemblies, each standard 17x17, < 20 t)j enriched to almost 5%, with burnable poisons, to give a four-year operating cycle between refuelling, which will involve replacing the entire core as a single cartridge. Core power density is lower than in a large PWR, and burn-up is about 35 GWd/t. (B&W draws upon over 50 years of experience in manufacturing nuclear propulsion systems for the US Navy, involving compact reactors with long core life.) A 60-year service life is envisaged, as sufficient used fuel storage would be built onsite for this.\n\nThe mPower reactor is modular in the sense that each unit is a factory-made module and several units would be combined into a power station of any size, but most likely a 380 MWe twin-unit plant and using approx 200 MWe turbine generators (also shipped as complete modules), constructed in three years. BWXT Nuclear Energy's present manufacturing capability in North America could produce these units.\n\nB&W Nuclear Energy Inc set up B&W Modular Nuclear Energy LLC (now BWXT mPower Inc) to market the design, in collaboration with Bechtel which joined the project as a 10% equity partner to design, license and deploy it. The company expects both design certification and construction permit in 2018, and commercial operation of the first two units in 2022. Overnight cost for a twin-unit plant was put by B&W at about $5000/kW.\n\nIn November 2013 B&W said it would seek to bring in further equity partners by mid-2014 to take forward the licensing and construction of an initial plant.\* B&W said it had invested $360 million in Generation mPower with Bechtel, and wanted to sell up to 70% of its stake in the joint venture, leaving it with about 20% and Bechtel 10%. In April 2014 B&W announced that it was cutting back funding on the project to about $15 million per year, having failed to find customers or investors. DOE then terminated further funding. B&W planned to retain the rights to manufacture the reactor module and nuclear fuel for the mPower plant. In December 2014 B&W finished laying off staff working on the project, and early in 2016 reduced funding further.\n\nWith more than $375 million having been spent on the mPower programme, in March 2016 BWXT and Bechtel reached agreement on “accelerated development” of the mPower project, so that Bechtel would take over leadership of the project and attempt for a year to secure funding for SMR development from third parties, including the DOE. If Bechtel succeeded in this, then BWXT and Bechtel would negotiate and execute a new agreement, with Bechtel taking over management of the mPower programme from BWXT. If Bechtel decided to terminate the project, it would be paid $30 million by BWXT, which is what happened in March 2017. The project was then shelved, leaving both BWXT and Bechtel free to be involved in the supply chain or management of other SMR projects.\n\n\* When B&W launched the mPower design in 2009, it said that Tennessee Valley Authority (TVA) would begin the process of evaluating Clinch River at Oak Ridge as a potential lead site for the mPower reactor, and that a memorandum of understanding had been signed by B&W, TVA and a consortium of regional municipal and cooperative utilities to explore the construction of a small fleet of mPower reactors. It was later reported that the other signatories of the agreement were FirstEnergy and Oglethorpe Power3. In February 2013 B&W signed an agreement with TVA to build up to four units at Clinch River, with design certification and construction permit application to be submitted to NRC in 2015. In August 2014 the TVA said it would file an early site permit (ESP) application instead of a construction permit application for one or more small modular reactors at Clinch River, possibly by the end of 2015. In February 2016 TVA said it was still developing a site at Oak Ridge for a SMR and would apply for an early site permit (ESP, with no technology identified) in May with a view to building up to 800 MWe of capacity there.",
"latitude": 37.413,
"longitude": -79.142,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Funding-for-mPower-reduced ||| Funding for mPower reduced ||| April 2014",
"newsLink2": "https://www.world-nuclear-news.org/Articles/mPower-simulator-in-action ||| mPower simulator in action ||| December 2012",
"newsLink3": "https://www.world-nuclear-news.org/Articles/mPower-empowered-by-SMR-funds ||| mPower empowered by SMR funds ||| November 2012"
},
{
"name": "MSR-1",
"developer": "Natura Resources",
"country": "USA",
"hqCity": "Texas",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 1,
"gross": 0.4,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 32.453007454074,
"longitude": -99.733484378974,
"newsLink1": "https://www.world-nuclear-news.org/articles/natura-ngl-collaboration-on-water-treatment ||| Natura, NGL collaboration on water treatment ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/construction-permit-granted-for-molten-salt-research-reactor ||| Construction permit granted for molten salt research reactor ||| September 2024",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Texas-partnership-to-investigate-MSR-deployment ||| Texas partnership to investigate MSR deployment ||| July 2024"
},
{
"name": "MSR-100",
"developer": "Natura Resources",
"country": "USA",
"hqCity": "Texas",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 250,
"gross": 100,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 32.453007454074,
"longitude": -99.733484378974,
"newsLink1": "https://www.world-nuclear-news.org/articles/natura-ngl-collaboration-on-water-treatment ||| Natura, NGL collaboration on water treatment ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/texas-partnership-evaluates-smr-use-for-water-desalination ||| Texas partnership evaluates SMR use for water desalination ||| February 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/four-smr-developers-aim-to-build-reactors-at-texas-am-university-site ||| Four SMR developers aim to build reactors at Texas A&M University site ||| February 2025"
},
{
"name": "Natrium",
"developer": "TerraPower",
"country": "USA",
"hqCity": "Bellevue",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 500,
"thermal": 840,
"gross": 345,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "GE with the US national laboratories had been developing a modular liquid metal-cooled inherently-safe reactor – PRISM (Power Reactor Innovative Small Module) – under the Advanced Liquid Metal Reactor/Integral Fast Reactor (ALMR/IFR) program funded by the US Department of Energy. The design is based on EBR-II and the original IFR. Another antecedent was GE's fast reactor power plant for USS Seawolf 1957-58. The ALMR/IFR program was cancelled in 1994 and no US fast neutron reactor has so far been larger than 66 MWe and none has supplied electricity commercially. However, the 1994 pre-application safety evaluation report13 for the original PRISM design concluded that \"no obvious impediments to licensing the PRISM design had been identified.\"\n\nToday's PRISM is a GE Hitachi (GEH) design for compact modular pool-type reactors with passive cooling for decay heat removal. After 30 years of development it represents GEH's Generation IV solution to closing the fuel cycle in the USA. Each PRISM power block consists of two modules of 311 MWe (840 MWt) each, (or, earlier, three modules of 155 MWe, 471 MWt), each with one steam generator, that collectively drive one turbine generator. The pool-type modules below ground level contain the complete primary system with sodium coolant at about 500°C. An intermediate sodium loop takes heat to steam generators. The metal Pu & DU fuel is obtained from used light water reactor fuel. All transuranic elements are removed together in the electrometallurgical reprocessing so that fresh fuel has minor actinides with the plutonium and uranium.\n\nThe reactor is designed to use a heterogeneous metal alloy core with 192 fuel assemblies in two fuel zones. In the version designed for used LWR fuel recycle, all these are fuel, giving peak burnup of 122 GWd/t. In other versions for breeding or weapons plutonium consumption, 42 of them are internal blanket and 42 are radial blanket, with 108 as driver fuel, and peak burnup of 144 GWd/t. For the LWR fuel recycle version, fuel stays in the reactor four years, with one-quarter removed annually, and 72 kg/yr net of fissile plutonium consumed. In the breeder version fuel stays in the reactor about six years, with one-third removed every two years, and net production of 57 kg/yr of fissile plutonium. Breeding ratio depends on purpose and hence configuration, so ranges from 0.72 for used LWR recycle to 1.23 for breeder. Used PRISM fuel is recycled after removal of fission products, though not necessarily into PRISM units.\nThe commercial-scale plant concept, part of an 'Advanced Recycling Center', would use three power blocks (six reactor modules) to provide 1866 MWe. In 2011 GE Hitachi announced that it was shifting its marketing strategy to pitch the reactor directly to utilities as a way to recycle excess plutonium while producing electricity for the grid. GEH bills it as a simplified design with passive safety features and using modular construction techniques. Its reference construction schedule is 36 months. In October 2016 GEH signed an agreement with Southern Nuclear Development, a subsidiary of Southern Nuclear Operating Company, to collaborate on licensing fast reactors including PRISM. In June 2017 GEH joined a team led by High Bridge Energy Development Co. and including Exelon Generation, High Bridge Associates and URS Nuclear to license PRISM.\nGEH is promoting to UK government agencies the potential use of PRISM technology to dispose of the UK's plutonium stockpile. Two PRISM units would irradiate fuel made from this plutonium (20% Pu, with DU and zirconium) for 45-90 days, bringing it to 'spent fuel standard' of radioactivity, after which it would be stored in air-cooled silos. The whole stockpile could be irradiated thus in five years, with some by-product electricity (but frequent interruptions for fuel changing) and the plant would then proceed to re-use it for about 55 years solely for 600 MWe of electricity generation, with one-third of the fuel being changed every two years. For this UK version, the breeding ratio is 0.8. No reprocessing plant ('Advanced Recycling Center') is envisaged initially, but this could be added later.\n\nIn March 2017 GEH and Advanced Reactor Concepts (see below) signed an agreement to collaborate on licensing an SMR design based on the ARC-100, but drawing on the extensive intellectual property and licensing experience of the GEH PRISM programme. Initial deployment is envisaged in Canada, at Point Lepreau in New Brunswick. ARC will seek a preliminary regulatory review with the CNSC through its Vendor Design Review process.\n\nIn February 2019 the US DOE launched its Versatile Test Reactor (VTR) programme, set up under the Nuclear Energy Innovation Capabilities Act 2017 and run by Idaho National Laboratory. The programme aims to provide the capability for testing advanced nuclear fuels, materials, instrumentation, and sensors. The VTR programme was effectively defunded when Congress zeroed its funding in FY2022. It would have been an adapted PRISM reactor to provide accelerated neutron damage rates 20 times greater than current water-cooled test reactors. (The only other fast research reactor operating is the BN-60 in Russia, to be replaced after 2020 by MBIR there.) In January 2020 GEH and TerraPower announced a collaboration to pursue a public-private partnership to design and construct the VTR for the DOE. They would be supported by the Energy Northwest utility consortium.\n\nA further collaboration between GE Hitachi and Terrapower is the Natrium concept. This is based on a PRISM reactor of 345 MWe and uses molten salt to store heat so that the output could be increased to about 500 MWe for up to five hours for load-following. The primary coolant is sodium, the secondary coolant is molten salt which can store heat or use it to make steam in a heat exchanger, switching between the two as required so that plant output can vary between 30% and 150% of reactor power. It would “help customers capitalize on peaking opportunities driven by renewable energy fluctuations.” Natrium is part of the DOE Advanced Reactor Demonstration Program (ARDP) offering funds on a cost-share basis and in October 2020 was awarded an initial grant of $80 million. In October 2020 Bechtel joined the consortium to provide design, licensing, procurement and construction services to the project.\n\nIn June 2021 TerraPower announced plans to build a demonstration Natrium unit in Wyoming at a retired coal plant site. TerraPower submitted a construction permit application to the NRC in March 2024 and held a groundbreaking ceremony in June 2024. The NRC completed its final safety evaluation in December 2025, with a construction permit expected in spring 2026. The total project cost is estimated at approximately $4 billion. In January 2026 Meta signed a deal with TerraPower for up to eight Natrium plants. ",
"latitude": 47.61,
"longitude": -122.201,
"newsLink1": "https://www.world-nuclear-news.org/articles/final-safety-evaluation-completed-for-wyoming-advanced-reactor ||| Final safety evaluation completed for Wyoming advanced reactor ||| December 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/terrapower-submits-natrium-for-uk-regulatory-assessment ||| TerraPower submits Natrium for UK regulatory assessment ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/terrapower-awards-natrium-supplier-contracts ||| TerraPower awards Natrium supplier contracts ||| July 2025"
},
{
"name": "NHR200-II",
"developer": "INET/Tsinghua University",
"country": "China",
"hqCity": "Beijing",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 278,
"thermal": 200,
"gross": 0,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The Chinese NHR-200 (Nuclear Heating Reactor), developed by Tsingua University's Institute of Nuclear Energy Technology (now the Institute of Nuclear and New Energy Technology), is a simple 200 MWt integral PWR design for district heating or desalination. It is based on the NHR-5 which was commissioned in 1989, and heated the INET campus for three wintersh.\n\nIt has convection circulation at 2.5 MPa in primary circuit pressure to produce steam at 127°C. Used fuel is stored around the core in the pressure vessel. The first NHR-200 plants are proposed for Daqing city in Heilongjiang province and Shenyang in Liaoning province.\n \nThe NHR200-II with design and verification tests concluded in 2016 operates at 8 MPa primary circuit pressure to produce steam at over 200°C and can also be used for power generation, seawater desalination or heat for mineral processing.",
"latitude": 40.006,
"longitude": 116.326,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Qinshan-plant-to-supply-district-heating ||| Qinshan plant to supply district heating ||| July 2021",
"newsLink2": "https://www.world-nuclear-news.org/Articles/CNNC-completes-design-of-district-heating-reactor ||| CNNC completes design of district heating reactor ||| September 2018",
"newsLink3": "https://www.world-nuclear-news.org/Articles/China-plans-demonstration-nuclear-heating-project ||| China plans demonstration nuclear heating project ||| February 2018"
},
{
"name": "Nuclearis N1",
"developer": "Nuclearis Energy",
"country": "USA",
"hqCity": "New York",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 320,
"thermal": 42,
"gross": 17,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "Nuclearis is developing pressurized water microreactors that are multi-functional, providing not only electricity but also heating and supporting industrial applications such as hydrogen production, hydrotreated vegetable oil biofuel, syngas, and biochar. By focusing on sectors that are traditionally difficult to decarbonise, the company aims to contribute to reducing carbon footprints across various industries. Its N1 microreactor design currently under development is expected to be constructed underground and operate without refueling for at least 20 years. At the end of its operational life, the reactor vessel transitions to a decay pool and dry storage solution, eliminating the need for external handling of used fuel.",
"latitude": 39.7539258803453,
"longitude": -75.5573848537544,
"newsLink1": "https://www.world-nuclear-news.org/articles/more-support-for-tripling-global-nuclear-capacity ||| More support for tripling global nuclear capacity ||| November 2025",
"newsLink2": "https://world-nuclear-news.org/articles/nuclearis-deepgeo-agree-to-collaborate ||| Nuclearis, DeepGeo agree to collaborate ||| April 2025",
"newsLink3": ""
},
{
"name": "Nuscale micro",
"developer": "NuScale Power",
"country": "USA",
"hqCity": "Corvallis",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": null,
"thermal": 50,
"gross": 1,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "In April 2019 NuScale announced that it was developing a 1-10 MWe \"simple and inherently safe compact heat pipe cooled reactor\" that \"requires little site infrastructure, can be rapidly deployed, and is fully automated during power operation.\" Partners include Additech, INL, and Oregon State University. The project follows solicitation of ideas and designs from the US Department of Defense and the Department of Energy. ",
"latitude": 45.431,
"longitude": -122.771,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "NuScale Power Module",
"developer": "NuScale Power",
"country": "USA",
"hqCity": "Corvallis",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 316,
"thermal": 250,
"gross": 77,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The NuScale Power Module is a 250 MWt, 77 MWe gross integral PWR with natural circulation.\* In December 2013 the US Department of Energy (DOE) announced that it would support accelerated development of the design for early deployment on a 50-50 cost share basis. An agreement for $217 million over five years was signed in May 2014 by NuScale Power. In September 2017, following acceptance of the company's design certification application (DCA) by the US Nuclear Regulatory Commission (NRC) earlier in the year, NuScale applied for the second part of its loan guarantee with the US DOE.\n\n\* In November 2020, it was announced that \"further value engineering efforts\" had resulted in the capacity of the NuScale Power Module being 25% higher than its previous value of 200 MWt, 60 MWe gross.\n\nIt will be factory-built with a three-metre diameter pressure vessel and convection cooling, with the only moving parts being the control rod drives. It uses standard PWR fuel enriched to 4.95% in normal PWR fuel assemblies (but which are only 2 m long), with 24-month refuelling cycle. Installed in a water-filled pool below ground level, the 4.6 m diameter, 23 m high cylindrical containment vessel module weighs 640 tonnes and contains the reactor with steam generator above it. A standard power plant would have 12 modules together giving about 924 MWe, though four-module and six-module plants are now envisaged also. The multi-unit plants are called VOYGR. An overhead crane would hoist each module from its pool to a separate part of the plant for refuelling. Design operational lifetime is 60 years. It has full passive cooling in operation and after shutdown for an indefinite period, without even DC battery requirement. The NRC concluded in January 2018 that NuScale's design eliminated the need for class 1E backup power – a current requirement for all US nuclear plants. It claims good load-following capability, in line with EPRI requirements and also black start capability.\n\nThe UK’s National Nuclear Laboratory (NNL) has confirmed that the reactor can run on MOX fuel. It also said that a VOYGR-12 plant with full MOX cores could consume 100 tonnes of reactor-grade plutonium in about 40 years, generating 200 TWh from it. This would be in line with Areva’s proposal for using the UK plutonium stockpile, especially since Areva is already contracted to make fuel for the NuScale reactor.\n\nThe company had estimated in 2010 that overnight capital cost for a 12-module, 540 MWe plant would be about $4000 per kilowatt, this in 2014 had risen to $5078/kWe net, with the levelized cost of electricity (LCOE) expected to be $100/MWh for first unit (or $90 for 'nth-of-a-kind'). In June 2018, the company announced that its reactor can generate 20% more power than originally planned. Subject to NRC approval, this would lower the overnight capital cost to about $4200 per kilowatt, and lower the LCOE by 18%. With a further power increase late in 2020 the company quoted a capital cost of $2850/kWe (for a 12-module 924 MWe plant).\n\nThe NuScale Power company was spun out of Oregon State University in 2007, though the original development was funded by the US Department of Energy. After NuScale experienced problems in funding its development, Fluor Corporation paid over $30 million for 55% of NuScale in October 2011. In May 2022 NuScale Power announced that it had merged with Spring Valley Acquisition Corp. The combined company, NuScale Power Corporation, is listed on the New York Stock Exchange. Fluor continues to hold a majority interest in the company, and provides it with engineering services, project management, and administration and supply chain support.\n\nIn April 2012 ARES Corporation agreed to assist in design and licensing. March 2014 Enercon Services became a partner to assist with design certification and licence applications. In October 2015 Ultra Electronics agreed to contribute technical expertise. In July 2019 Doosan Heavy Industries brought its pressure vessel manufacturing ability to the project and followed this with $104 million equity. Also in July 2019 Sargent & Lundy agreed to support the plant design. In April 2021 Japan’s JGC Holdings agreed to invest $40 million and, as EPC contractor, to partner with Fluor in deployment of NuScale SMRs. In May 2021 Japan’s IHI invested $20 million cash and became a strategic partner. In June 2021 GS Energy North America joined them, as did Samsung in July. All these contributed equity to NuScale, though leaving Fluor as majority and lead strategic investor.\n\nNuScale lodged an application for US design certification in January 2017, and in July 2017 the NRC confirmed that its highly integrated protection system (HIPS) architecture was approved. NuScale has been engaged with the NRC since 2008, having spent some $130 million on licensing to November 2013. In September 2020 the NRC issued a standard design approval for the earlier 50 MWe version.\* NuScale said it would apply in 2022 for the same approval for the 60 MWe version, although later, in November 2020, the company announced that each module would now be 77 MWe. It is the first SMR to receive NRC design approval. In October 2022 the NRC said it agreed with NuScale’s methodology for calculating the emergency planning zone (EPZ) for use with NuScale’s design. In May 2025 the NRC issued a standard design approval for the 77 MWe version.\n\n\* The standard design approval (SDA) allows the NuScale standard design to be referenced in an application for a construction permit or operating licence, or an application for a combined construction and operating licence (COL) under NRC regulations. Site-specific licensing procedures must also be completed before any construction can begin.\n\nIn September 2018 NuScale selected BWX Technologies as the first manufacturer of its SMR after an 18-month selection process. The demonstration unit in Idaho will have dry cooling for the condenser circuit, with a 90% water saving while sacrificing about 5% of its power output to drive the cooling. In mid-2021 Doosan said it was preparing to start the forging fabrication for UAMPS reactor modules in 2022 and Samsung said that NuScale, Fluor and Samsung C&T Corporation would work together to deliver NuScale plants globally.\nIn December 2019 NuScale submitted its 60 MWe (now 77 MWe) SMR design to the Canadian Nuclear Safety Commission (CNSC) for pre-licensing vendor design review. Phase 2 of this commenced in January 2020.\n\nEarlier in March 2012 the DOE signed an agreement with NuScale regarding constructing a demonstration unit at its Savannah River Site in South Carolina.\n\nIn mid-2013 NuScale launched the Western Initiative for Nuclear (WIN) – a broad, multi-western state collaboration\* – to study the demonstration and deployment of a multi-module NuScale SMR plant in western USA. This became the Carbon-Free Power Project led by Utah Associated Municipal Power Systems (UAMPS) at the DOE’s Idaho National Laboratory (INL). However, the project was cancelled in November 2023, citing rising costs.\n\nWIN includes Energy Northwest (ENW) in Washington and Utah Associated Municipal Power Systems (UAMPS). A demonstration NuScale SMR was planned as part of Project WIN at the DOE's Idaho National Laboratory (INL), with UAMPS as the owner and ENW the operator, but the project was cancelled in November 2023. This was to be followed by a full-scale (originally planned as 12- but now six-module) plant owned by UAMPS and run by Energy Northwest. With the unit power to increase to 77 MWe, the cost of a 12-module plant would be about $2850/kW on an overnight basis. Energy Northwest comprises 27 public utilities, and had examined small reactor possibilities before choosing NuScale and becoming part of the UAMPS Carbon-Free Power Project. UAMPS is targeting $55/MWh generation cost (LCOE).\n\* Washington, Oregon, Idaho, Wyoming, Utah and Arizona.\n\nIn Poland, NuScale is exploring with Unimot and KGHM possibilities for its reactors to replace coal-fired power plants.\nNuScale is investigating cogeneration options including desalination (with Aquatech), oil recovery from tar sands and refinery power (with Fluor), hydrogen production by high-temperature steam electrolysis (with INL) and flexible back-up for a wind farm (with UAMPS and Energy Northwest). Doosan is cooperating on hydrogen production and desalination.\n\nNuScale and Prodigy Clean Energy are developing a floating version of NuScale’s SMR that could be deployed at sea close to shorelines.\nIn December 2022 NuScale announced it had completed the standard generic plant design for the VOYGR plant that would serve as a starting point for deploying site-specific designs. \n\nIn September 2025 NuScale announced the ENTRA1 Energy partnership and signed a memorandum of understanding with the Tennessee Valley Authority for up to 6 GW of NuScale SMR capacity. NuScale is also developing the RoPower project in Romania with Nuclearelectrica. FID was reached for the project in February 2026.",
"latitude": 45.431,
"longitude": -122.771,
"newsLink1": "https://www.world-nuclear-news.org/articles/final-investment-decision-taken-for-romanias-smrs ||| Final Investment Decision taken for Romanian SMR project ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/joint-study-validates-smr-use-for-chemical-plants ||| Joint study validates SMR use for chemical plants ||| January 2026",
"newsLink3": "https://www.world-nuclear-news.org/articles/nuscale-integrated-energy-system-desalination-clean-hydrogen ||| NuScale targets integrated energy system for desalination and clean hydrogen ||| June 2025"
},
{
"name": "NUWARD",
"developer": "EDF",
"country": "France",
"hqCity": "Paris",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 307,
"thermal": 540,
"gross": 170,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "TechnicAtome with Naval Group and CEA in France have developed the NP-300 PWR design from naval power plants and aimed it at export markets for power, heat and desalination. It is a PWR with passive safety systems and could be built for applications of 100 to 300 MWe or more with up to 500,000 m3/day desalination. As of mid-2018, a 570 MWt/170 MWe version was proposed, in a metallic compact containment submerged in water. In September 2019 twin 170 MWe units were proposed to comprise a 340 MWe power plant, with two reactors sharing a pool. A partnership with Westinghouse was being considered. EdF planned to enter the basic design pre-licensing phase with ASN in 2022. Some €1 billion state funding was promised for the project. However, in July 2024 EDF abandoned the twin-reactor concept in favour of a single 400 MWe PWR, designated NUWARD SM400. A Phase 3 joint European regulatory review involving eight national regulators was launched in January 2026.\n\nEDF is \"targeting replacing ageing coal plants of the 300 to 400 MW range\" with two-unit Nuward plants, as well as at supplying remote municipalities and energy intensive industrial sites and powering small grids. \nTechnicAtome makes the K15 naval reactor of 150 MWt, running on low-enriched fuel. A land-based equivalent – Réacteur d’essais à terre (RES) – was built at Cadarache from 2003 with several delays and achieved criticality in October 2018. It is essentially a PWR test reactor for the Navy. \n\nIt earlier seemed that some version of this reactor might be used in the Flexblue submerged nuclear power plant being proposed by DCNS in France, but now cancelled. The concept eliminated the need for civil engineering, and refuelling or major service could be undertaken by refloating it and returning to the shipyard.",
"latitude": 48.892,
"longitude": 2.258,
"newsLink1": "https://www.world-nuclear-news.org/articles/international-safety-assessments-of-finnish-french-smrs ||| International safety assessments of Finnish, French SMRs ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/second-phase-of-nuward-review-completed ||| Second phase of Nuward review completed ||| December 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/edf-simplifies-nuward-smr-design ||| EDF simplifies Nuward SMR design ||| January 2025"
},
{
"name": "ODIN",
"developer": "NANO Nuclear Energy",
"country": "USA",
"hqCity": "New York",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 400,
"thermal": 5,
"gross": 2,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 40.7128,
"longitude": -74.006,
"newsLink1": "https://www.world-nuclear-news.org/articles/british-firm-to-acquire-odin-microreactor-design ||| British firm to acquire ODIN microreactor design ||| September 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/nano-reactor-core-block-ready-for-testing ||| NANO reactor core block ready for testing ||| March 2025",
"newsLink3": "https://world-nuclear-news.org/articles/microreactor-company-announces-flurry-of-mous ||| Microreactor company announces flurry of MoUs ||| December 2024"
},
{
"name": "Otrera",
"developer": "Otrera New Energy",
"country": "France",
"hqCity": "Aix-en-Provence",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 550,
"thermal": 300,
"gross": 110,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 43.4921567660575,
"longitude": 5.331110406198648,
"newsLink1": "https://www.world-nuclear-news.org/articles/orano-sets-up-working-groups-for-fast-reactor-fuels ||| Orano sets up working groups for fast reactor fuels ||| October 2024",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "PB-FHR",
"developer": "UC Berkeley",
"country": "USA",
"hqCity": "Berkeley",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 236,
"gross": 100,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "This was a pre-conceptual US design completed in 2014 to evaluate the potential benefits of fluoride high-temperature reactor (FHR) technology. A consortium including University of California Berkeley, Oak Ridge National Laboratory and Westinghouse designed it as a 236 MWt/100 MWe pebble-bed FHR, with annular core, operating at 700°C. It is designed for modular construction, and from 100 MWe base-load it is able to deliver 240 MWe with gas co-firing for peak loads. Fuel pebbles are 30 mm diameter, much less than gas-cooled HTRs. The project looked at how FHRs might be coupled to a Brayton combined-cycle turbine to generate power, design of a passive decay heat removal system, and the annular pebble bed core. The PB-FHR has negative void reactivity and passive decay heat removal.",
"latitude": 37.8715,
"longitude": -122.273,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "PBMR-400",
"developer": "PBMR (Pty)",
"country": "South Africa",
"hqCity": "Centurion",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 900,
"thermal": 400,
"gross": 165,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "South Africa's pebble bed modular reactor (PBMR) was being developed by the PBMR (Pty) Ltd consortium led by the utility Eskom, latterly with involvement of Mitsubishi Heavy Industries, and drew on German expertise, notably the HTR-Modul design. It aimed for a step change in safety, economics and proliferation resistance. Full-scale production units had been planned to be 400 MWt (165 MWe) but more recent plans were for 200 MWt (80 MWe)7. Financial constraints led to delays8 and in September 2010 the South African government confirmed it would stop funding the project9 and closed it down.\n\nThe earlier plans for the 400 MWt PBMR following a 2002 review envisaged a direct cycle (Brayton cycle) gas turbine generator and thermal efficiency about 41%, the helium coolant leaving the bottom of the core at about 900°C and driving a turbine. Power would be adjusted by changing the pressure in the system. The helium is passed through a water-cooled pre-cooler and intercooler before being returned to the reactor vessel. The PBMR Demonstration Power Plant (DPP) was expected to start construction at Koeberg in 2009 and achieve criticality in 2013, but after this was delayed it was decided to focus on the 200 MWt design.\n\nThe 200 MWt (80 MWe) later design announced in 2009 was to use a conventional Rankine cycle, enabling the PBMR to deliver super-heated steam via a steam generator as well as generate electricity. This design \"is aimed at steam process heat applications operating at 720°C, which provides the basis for penetrating the nuclear heat market as a viable alternative for carbon-burning, high-emission heat sources.\"10 An agreement with Mitsubishi Heavy Industries to take forward the R&D on this design was signed in February 2010. MHI had been involved in the project since 2001, having done the basic design and R&D of the helium-driven turbogenerator system and core barrel assembly, the major components of the 400 MWt direct-cycle design.\n\nThe PBMR has a vertical steel reactor pressure vessel which contains and supports a metallic core barrel, which in turn supports the cylindrical pebble fuel core. This core is surrounded on the side by an outer graphite reflector and on top and bottom by graphite structures which provide similar upper and lower neutron reflection functions. Vertical borings in the side reflector are provided for the reactivity control elements. Some 360,000 fuel pebbles (silicon carbide-coated 9.6% enriched uranium dioxide particles encased in graphite spheres of 60 mm diameter) cycle through the reactor continuously (about six times each) until they are expended after about three years. This means that a reactor would require 12 total fuel loads in its design lifetime.\n\nA pebble fuel plant at Pelindaba was planned. Meanwhile, the company produced some fuel which was successfully tested in Russia.\n\nThe PBMR was proposed for the US Next Generation Nuclear Plant project and submission of an application for design certification reached the pre-application review stage, but is now listed as 'inactive' by the NRC. The company was part of the National Project Management Corporation (NPMC) consortium which applied for the second round of DOE funding in 2013. This 2013 application for federal funds appeared to revive the earlier direct-cycle PBMR design, emphasising its ‘deep burn’ attributes in destroying actinides and achieving high burn-up at high temperatures.\n\nIn 2016 Eskom revived consideration of a reactor based on the PBMR, with a view to developing a design that is simpler and more efficient than the original, and also looking at applications for process heat that were not fully explored by the original R&D programme. However, most of the scientific and engineering staff had emigrated, many of them to the USA and many joined X-energy’s similar project.\n\nA new concept was for an advanced high-temperature reactor of 150 MWe to be deployed in the 2030s, with a 50 MWe pilot plant built in the mid-2020s. It would be a combined-cycle plant with gas flow now from bottom to top, and the temperature will be much higher. The pressure vessel would be concrete, and it would have a pebble bed reactor core. Helium would exit the reactor to a gas turbine at 1200°C, and the exhaust gas from this at 600°C would drive a steam cycle, using a molten salt circuit, with overall 60% thermal efficiency. The gas turbine would produce 40% of the power, the steam cycle 60%.\n\nA further conceptual design is the HTMR-100, a 35 MWe (100 MWt) pebble bed HTR for electricity or process heat. The conceptual design, commenced in 2012, from Steenkampskraal Thorium Limited (STL) in South Africa, was completed in 2018. Also known as the Th-100, it is derived from the Jülich and PBMR designs. For electricity, single units have load-following capability, or four can comprise a 140 MWe power plant. There are a range of fuel options involving LEU, thorium and reactor-grade plutonium, with burn-up of 80-90 GWd/t of TRISO fuel pebbles. It has a graphite moderator and helium coolant at 750°C, and a single pass fuel cycle. The reactor vessel is 15 m high, 5.9 m diameter and primary loop pressure is relatively low at 4 MPa.",
"latitude": -25.86,
"longitude": 28.189,
"newsLink1": "https://www.world-nuclear-news.org/articles/south-africa-lifts-pbmr-from-care-and-maintenance ||| South Africa lifts PBMR from care and maintenance ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/south-africa-government-reiterates-commitment-to-new-nuclear-and-pbmr ||| South Africa 'committed to new nuclear and PBMR' ||| December 2024",
"newsLink3": "https://www.world-nuclear-news.org/articles/south-africa-aims-to-be-global-supplier-of-htr-fue ||| South Africa aims to be global supplier of HTR fuel ||| March 2024"
},
{
"name": "PeLUIt/RDE",
"developer": "BATAN",
"country": "Indonesia",
"hqCity": "Jakarta",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 10,
"gross": 3,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": -6.2,
"longitude": 106.816,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Batan-to-cooperate-with-Indonesian-power-company ||| Batan to cooperate with Indonesian power company ||| August 2019",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Indonesia-extends-nuclear-cooperation-with-China ||| Indonesia extends nuclear cooperation with China ||| August 2018",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Progress-with-Indonesian-SMR-project ||| Progress with Indonesian SMR project ||| March 2018"
},
{
"name": "PHWR-220",
"developer": "NPCIL",
"country": "India",
"hqCity": "Mumbai",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 310,
"thermal": 755,
"gross": 220,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": false,
"offGrid": false,
"notes": "These are the oldest and smallest of the Indian pressurized heavy water reactor (PHWR) range, with a total of 16 now online, 800 MWt, 220 MWe gross typically. Rajasthan 1 was built as a collaborative venture between Atomic Energy of Canada Ltd (AECL) and the Nuclear Power Corporation of India (NPCIL), starting up in 1972. Subsequent indigenous PHWR development has been based on these units, though several stages of evolution can be identified: PHWRs with dousing and single containment at Rajasthan 1&2, PHWRs with suppression pool and partial double containment at Madras, and later standardized PHWRs from Narora onwards having double containment, suppression pool, and calandria filled with heavy water, housed in a water-filled calandria vault. They are moderated and cooled by heavy water, and the natural uranium oxide fuel is in horizontal pressure tubes, allowing refuelling online (maintenance outages are scheduled after 24 months). Burn-up is about 15 GWd/t.",
"latitude": 19.046,
"longitude": 72.928,
"newsLink1": "https://www.world-nuclear-news.org/articles/minister-updates-parliament-on-indian-smr-project ||| Minister updates parliament on Indian SMR project ||| March 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/npcil-seeks-proposals-for-privately-funded-small-reactor-projects ||| India's NPCIL seeks proposals for privately funded small reactor projects ||| January 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/milestones-for-rajasthan-reactors-old-and-new ||| Milestones for Rajasthan reactors old and new ||| August 2024"
},
{
"name": "PRISM",
"developer": "GE Hitachi",
"country": "USA",
"hqCity": "Wilmington",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 500,
"thermal": 840,
"gross": 311,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "GE with the US national laboratories had been developing a modular liquid metal-cooled inherently-safe reactor – PRISM (Power Reactor Innovative Small Module) – under the Advanced Liquid Metal Reactor/Integral Fast Reactor (ALMR/IFR) program funded by the US Department of Energy. The design is based on EBR-II and the original IFR. Another antecedent was GE's fast reactor power plant for USS Seawolf 1957-58. The ALMR/IFR program was cancelled in 1994 and no US fast neutron reactor has so far been larger than 66 MWe and none has supplied electricity commercially. However, the 1994 pre-application safety evaluation report13 for the original PRISM design concluded that \"no obvious impediments to licensing the PRISM design had been identified.\"\n\nToday's PRISM is a GE Hitachi (GEH) design for compact modular pool-type reactors with passive cooling for decay heat removal. After 30 years of development it represents GEH's Generation IV solution to closing the fuel cycle in the USA. Each PRISM power block consists of two modules of 311 MWe (840 MWt) each, (or, earlier, three modules of 155 MWe, 471 MWt), each with one steam generator, that collectively drive one turbine generator. The pool-type modules below ground level contain the complete primary system with sodium coolant at about 500°C. An intermediate sodium loop takes heat to steam generators. The metal Pu & DU fuel is obtained from used light water reactor fuel. All transuranic elements are removed together in the electrometallurgical reprocessing so that fresh fuel has minor actinides with the plutonium and uranium.\n\nThe reactor is designed to use a heterogeneous metal alloy core with 192 fuel assemblies in two fuel zones. In the version designed for used LWR fuel recycle, all these are fuel, giving peak burnup of 122 GWd/t. In other versions for breeding or weapons plutonium consumption, 42 of them are internal blanket and 42 are radial blanket, with 108 as driver fuel, and peak burnup of 144 GWd/t. For the LWR fuel recycle version, fuel stays in the reactor four years, with one-quarter removed annually, and 72 kg/yr net of fissile plutonium consumed. In the breeder version fuel stays in the reactor about six years, with one-third removed every two years, and net production of 57 kg/yr of fissile plutonium. Breeding ratio depends on purpose and hence configuration, so ranges from 0.72 for used LWR recycle to 1.23 for breeder. Used PRISM fuel is recycled after removal of fission products, though not necessarily into PRISM units.\nThe commercial-scale plant concept, part of an 'Advanced Recycling Center', would use three power blocks (six reactor modules) to provide 1866 MWe. In 2011 GE Hitachi announced that it was shifting its marketing strategy to pitch the reactor directly to utilities as a way to recycle excess plutonium while producing electricity for the grid. GEH bills it as a simplified design with passive safety features and using modular construction techniques. Its reference construction schedule is 36 months. In October 2016 GEH signed an agreement with Southern Nuclear Development, a subsidiary of Southern Nuclear Operating Company, to collaborate on licensing fast reactors including PRISM. In June 2017 GEH joined a team led by High Bridge Energy Development Co. and including Exelon Generation, High Bridge Associates and URS Nuclear to license PRISM.\nGEH is promoting to UK government agencies the potential use of PRISM technology to dispose of the UK's plutonium stockpile. Two PRISM units would irradiate fuel made from this plutonium (20% Pu, with DU and zirconium) for 45-90 days, bringing it to 'spent fuel standard' of radioactivity, after which it would be stored in air-cooled silos. The whole stockpile could be irradiated thus in five years, with some by-product electricity (but frequent interruptions for fuel changing) and the plant would then proceed to re-use it for about 55 years solely for 600 MWe of electricity generation, with one-third of the fuel being changed every two years. For this UK version, the breeding ratio is 0.8. No reprocessing plant ('Advanced Recycling Center') is envisaged initially, but this could be added later.\n\nIn March 2017 GEH and Advanced Reactor Concepts (see below) signed an agreement to collaborate on licensing an SMR design based on the ARC-100, but drawing on the extensive intellectual property and licensing experience of the GEH PRISM programme. Initial deployment is envisaged in Canada, at Point Lepreau in New Brunswick. ARC will seek a preliminary regulatory review with the CNSC through its Vendor Design Review process.\n\nIn February 2019 the US DOE launched its Versatile Test Reactor (VTR) programme, set up under the Nuclear Energy Innovation Capabilities Act 2017 and run by Idaho National Laboratory. The programme aims to provide the capability for testing advanced nuclear fuels, materials, instrumentation, and sensors. The VTR, which is intended to be operational at INL by the end of 2025, would be an adapted PRISM reactor to provide accelerated neutron damage rates 20 times greater than current water-cooled test reactors. (The only other fast research reactor operating is the BN-60 in Russia, to be replaced after 2020 by MBIR there.) In January 2020 GEH and TerraPower announced a collaboration to pursue a public-private partnership to design and construct the VTR for the DOE. They would be supported by the Energy Northwest utility consortium.\n\nA further collaboration between GE Hitachi and Terrapower is the Natrium concept. This is based on a PRISM reactor of 345 MWe and uses molten salt to store heat so that the output could be increased to about 500 MWe for up to five hours for load-following. The primary coolant is sodium, the secondary coolant is molten salt which can store heat or use it to make steam in a heat exchanger, switching between the two as required so that plant output can vary between 30% and 150% of reactor power. It would “help customers capitalize on peaking opportunities driven by renewable energy fluctuations.” Natrium is part of the DOE Advanced Reactor Demonstration Program (ARDP) offering funds on a cost-share basis and in October 2020 was awarded an initial grant of $80 million. In October 2020 Bechtel joined the consortium to provide design, licensing, procurement and construction services to the project.\n\nIn June 2021 TerraPower announced plans to build a demonstration Natrium unit in Wyoming at a retired coal plant site. It plans to submit a construction permit application in 2023 and an operating licence application in 2026. The plant is expected to cost under $1 billion apart from financing. ",
"latitude": 34.21,
"longitude": -77.882,
"newsLink1": "https://www.world-nuclear-news.org/Articles/DOE-formalises-test-reactor-decision ||| DOE formalises test reactor decision ||| July 2022",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Final-environmental-impact-statement-for-US-Versat ||| Final environmental impact statement for US Versatile Test Reactor ||| May 2022",
"newsLink3": "https://www.world-nuclear-news.org/articles/prism-selected-for-us-test-reactor-programme ||| PRISM selected for US test reactor programme ||| November 2018"
},
{
"name": "PWR-20",
"developer": "Last Energy",
"country": "USA",
"hqCity": "Washington D.C",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 331,
"thermal": 80,
"gross": 20,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 38.9072,
"longitude": -77.0369,
"newsLink1": "https://www.world-nuclear-news.org/articles/last-energy-microreactor-planned-at-texas-university ||| Last Energy microreactor planned at Texas university ||| October 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/regulatory-progress-for-last-energys-uk-project ||| Regulatory progress for Last Energy's UK project ||| July 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/last-energy-plans-texan-microreactor-plant ||| Last Energy plans Texan microreactor plant ||| February 2025"
},
{
"name": "R1",
"developer": "Antares Nuclear",
"country": "USA",
"hqCity": "California",
"reactorType": "Heat pipe-cooled",
"spectrum": "Thermal",
"outletTemp": 800,
"thermal": 1,
"gross": 0.3,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 33.8546606660001,
"longitude": -118.344679438837,
"newsLink1": "https://www.world-nuclear-news.org/articles/triso-fuel-progress-for-us-reactor-pilot-programme ||| TRISO fuel progress for US reactor pilot programme ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/doe-announces-first-selections-for-pilot-reactor-programme ||| DOE announces first selections for pilot reactor programme ||| August 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/final-gain-vouchers-for-2024-announced ||| Final GAIN vouchers for 2024 announced ||| September 2024"
},
{
"name": "Rapid-L",
"developer": "CRIEPI",
"country": "Japan",
"hqCity": "Tokyo",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 550,
"thermal": 5,
"gross": 0.2,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": false,
"highTempHeat": true,
"offGrid": false,
"notes": "A small-scale design developed by Japan's Central Research Institute of Electric Power Industry (CRIEPI) in cooperation with Mitsubishi Research Institute and funded by the Japan Atomic Energy Research Institute (JAERI) is the 5 MWt, 200 kWe Rapid-L, using lithium-6 (a neutron poison) as control medium. It would have 2700 fuel pins of 40-50% enriched uranium nitride with 2600°C melting point integrated into a disposable cartridge or 'integrated fuel assembly'. The reactivity control system is passive, using lithium expansion modules (LEMs) which give burn-up compensation, partial load operation as well as negative reactivity feedback. During normal operation, lithium-6 in the LEM is suspended on an inert gas above the core region. As the reactor temperature rises, the lithium-6 expands, moving the gas/liquid interface down into the core and hence adding negative reactivity. Other kinds of lithium modules, also integrated into the fuel cartridge, shut down and start up the reactor. Cooling is by molten sodium, and with the LEM control system, reactor power is proportional to primary coolant flow rate. Refuelling would be every 10 years in an inert gas environment. Operation would require no skill, due to the inherent safety design features. The whole plant would be about 6.5 metres high and 2 metres diameter.\n\nThe larger RAPID reactor delivers 1 MWe and is U-Pu-Zr fuelled and sodium-cooled",
"latitude": 35.637,
"longitude": 139.579,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "RITM-200M",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 321,
"thermal": 198,
"gross": 50,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "RITM series is Russia's 'flagship' SMR design. The compact RITM-200M will replace the KLT reactors to serve in floating nuclear power plants, or optimized floating power units (OFPUs) as they are now called by OKBM. It is derived from the OKBM Afrikantov's RITM-200 reactor units in the LK-60 icebreakers and is an integral 175 MWt/50 MWe PWR with 12 steam generator cassettes inside the pressure vessel and four coolant loops with external main circulation pumps. It has inherent safety features, using low-enriched (<20%) fuel in 241 fuel assemblies (compared with 199 in the icebreaker version). OFPUs will be returned to base for servicing every 10 or 12 years and no onboard used fuel storage is required. Operational lifetime is 60 years. Twin reactor units in containment have a mass of 2600 tonnes and occupy 6.8 m × 14.6 m × 16.0 m high, requiring only a 12,000 tonne barge – much smaller than the KLT-40S units. A major challenge is the reliability of steam generators and associated equipment which are much less accessible when inside the reactor pressure vessel.\n\nRosatom is planning three OFPUs each with twin RITM-200M reactors at Cape Nagloynyn to supply 330 MWe to the Baimskaya copper mining project south of Bilibino and Pevek.\n\nOnshore installation of the similar RITM-200N is also envisaged, with one or more modules of 190 MWt/55 MWe, fuel enriched to almost 20% and 5-6 year fuel cycle. Reactor containment dimensions are 6 m × 6 m × 15.5 m. The first plant is to be in Ust-Kuyga in Yakutia. Rostechnadzor licensed this in August 2021, with site preparation underway and operation expected around 2028-2029. This will be a reference plant for export sales. In May 2024 Rosatom signed a contract with Uzbekistan for six RITM-200N units to supply approximately 330 MWe.\n\nThe RITM-200B is a 209 MWt version and the RITM-400 is a 315 MWt version, both for icebreaker use.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://www.world-nuclear-news.org/articles/eight-ritm-reactors-currently-under-production ||| Eight RITM reactors currently under production ||| March 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/russias-floating-nuclear-power-plant-passes-one-billion-kwh ||| Russia's floating nuclear power plant passes one billion kWh ||| January 2025",
"newsLink3": "https://world-nuclear-news.org/Articles/Q-A-The-prospects-for-floating-nuclear-power-plant ||| Q&A: The prospects for floating nuclear power plants ||| May 2024"
},
{
"name": "RITM-200N",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 321,
"thermal": 190,
"gross": 55,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "RITM series is Russia's 'flagship' SMR design. The compact RITM-200M will replace the KLT reactors to serve in floating nuclear power plants, or optimized floating power units (OFPUs) as they are now called by OKBM. It is derived from the OKBM Afrikantov's RITM-200 reactor units in the LK-60 icebreakers and is an integral 175 MWt/50 MWe PWR with 12 steam generator cassettes inside the pressure vessel and four coolant loops with external main circulation pumps. It has inherent safety features, using low-enriched (<20%) fuel in 241 fuel assemblies (compared with 199 in the icebreaker version). OFPUs will be returned to base for servicing every 10 or 12 years and no onboard used fuel storage is required. Operational lifetime is 60 years. Twin reactor units in containment have a mass of 2600 tonnes and occupy 6.8 m × 14.6 m × 16.0 m high, requiring only a 12,000 tonne barge – much smaller than the KLT-40S units. A major challenge is the reliability of steam generators and associated equipment which are much less accessible when inside the reactor pressure vessel.\n\nRosatom is planning three OFPUs each with twin RITM-200M reactors at Cape Nagloynyn to supply 330 MWe to the Baimskaya copper mining project south of Bilibino and Pevek.\n\nOnshore installation of the similar RITM-200N is also envisaged, with one or more modules of 190 MWt/55 MWe, fuel enriched to almost 20% and 5-6 year fuel cycle. Reactor containment dimensions are 6 m × 6 m × 15.5 m. The first plant is to be in Ust-Kuyga in Yakutia. Rostechnadzor licensed this in August 2021, with construction to begin in 2024 and operation expected in 2028. This will be a reference plant for export sales.\n\nThe RITM-200B is a 209 MWt version and the RITM-400 is a 315 MWt version, both for icebreaker use.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://www.world-nuclear-news.org/articles/excavation-works-begin-for-uzbek-small-modular-reactor ||| Excavation works begin for Uzbekistan small modular reactor ||| October 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/uzbekistan-smr-project-sees-start-of-auxiliary-buildings-construction ||| Uzbekistan SMR project sees start of auxiliary buildings construction ||| April 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/eight-ritm-reactors-currently-under-production ||| Eight RITM reactors currently under production ||| March 2025"
},
{
"name": "RITM-200S",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 321,
"thermal": 198,
"gross": 50,
"fuelEnrichment": "5-20%",
"designStatus": "Under construction",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "RITM series is Russia's 'flagship' SMR design. The compact RITM-200M will replace the KLT reactors to serve in floating nuclear power plants, or optimized floating power units (OFPUs) as they are now called by OKBM. It is derived from the OKBM Afrikantov's RITM-200 reactor units in the LK-60 icebreakers and is an integral 175 MWt/50 MWe PWR with 12 steam generator cassettes inside the pressure vessel and four coolant loops with external main circulation pumps. It has inherent safety features, using low-enriched (<20%) fuel in 241 fuel assemblies (compared with 199 in the icebreaker version). OFPUs will be returned to base for servicing every 10 or 12 years and no onboard used fuel storage is required. Operational lifetime is 60 years. Twin reactor units in containment have a mass of 2600 tonnes and occupy 6.8 m × 14.6 m × 16.0 m high, requiring only a 12,000 tonne barge – much smaller than the KLT-40S units. A major challenge is the reliability of steam generators and associated equipment which are much less accessible when inside the reactor pressure vessel.\n\nRosatom is planning three OFPUs each with twin RITM-200M reactors at Cape Nagloynyn to supply 330 MWe to the Baimskaya copper mining project south of Bilibino and Pevek.\n\nOnshore installation of the similar RITM-200N is also envisaged, with one or more modules of 190 MWt/55 MWe, fuel enriched to almost 20% and 5-6 year fuel cycle. Reactor containment dimensions are 6 m × 6 m × 15.5 m. The first plant is to be in Ust-Kuyga in Yakutia. Rostechnadzor licensed this in August 2021, with construction to begin in 2024 and operation expected in 2028. This will be a reference plant for export sales.\n\nThe RITM-200B is a 209 MWt version and the RITM-400 is a 315 MWt version, both for icebreaker use.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://world-nuclear-news.org/Articles/Nuclear-fuel-development-completed-for-RITM-200S-f ||| Development of nuclear fuel 'complete' for RITM-200S floating power project ||| December 2022",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Construction-starts-on-Russia-s-next-floating-nucl ||| Construction starts on Russia's next floating nuclear power plant ||| August 2022",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Construction-starts-on-Russia-s-next-floating-nucl ||| Construction starts on Russias next floating nuclear power plant ||| May 2022"
},
{
"name": "Rolls-Royce SMR",
"developer": "Rolls-Royce",
"country": "United Kingdom",
"hqCity": "Derby",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 322,
"thermal": 1358,
"gross": 470,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "Rolls-Royce has been working since 2015 on a design that was originally 220 MWe, but the focus has changed to a medium-sized reactor of 400-440 MWe (1200-1350 MWt), and from 2021 was referred to as \"at least 470 MW\". It is a three-loop PWR with close-coupled external steam generators. It is to be factory-built, with major components transportable to site (RPV: 11.3 m high, 4.5 m diameter, SG: 4.95 m diameter, about 25 m high) and assembled in 500 days. It has a 60-year design operating lifetime. It would use 4.95% enriched fuel with 55-60 GWd/t burn-up in 121 standard PWR fuel assemblies with active fuelled length of 2.8 m and using burnable poison in 40 out of 264 fuel rods in each. The refuelling cycle would be 18-24 months. One such unit would comprise a stand-alone power plant.\n\nEarly in 2016 Rolls-Royce submitted a detailed design to the UK government for a 220 MWe SMR unit and also a paper to the Department of Business, Energy and Industrial Strategy, outlining its plan to develop a fleet of 7 GWe of SMRs in the UK with a new consortium, plus 9 GWe of exported units. In 2020 the partners with Rolls-Royce were: Assystem, Atkins, BAM Nuttall, Laing O'Rourke, National Nuclear Laboratory, Nuclear AMRC, Jacobs and The Welding Institute; and in November 2020 it added US utility Exelon with a view to it operating Rolls-Royce SMRs in the UK and abroad. Its focus is on existing licensed nuclear sites in the UK, notably Trawsfynydd in north Wales, the site of a former Magnox nuclear power station. The first unit is expected in the mid-2030s.\n\nIn May 2021 the cost of a 470 MWe unit was put at about £1.8 billion, so $5100/kW, and levelized cost of electricity (LCOE) at £35-50/MWh. The company submitted the design for the UK generic design assessment (GDA) process in November 2021, and in March 2022 the ONR began the GDA. Step 2 was completed in July 2024, and Step 3 is in progress with completion expected by August 2026. In November 2025 Wylfa in north Wales was confirmed as the first site. UK government funding of £2.5 billion has been committed to the programme.\n\nIn November 2017, Rolls-Royce signed a memorandum of understanding (MoU) with the Jordan Atomic Energy Commission to conduct a technical feasibility study for the construction of a Rolls-Royce SMR in the Middle Eastern country. In March 2020, Turkey's state-owned EUAS International ICC signed an MoU with Rolls-Royce to evaluate the technical, economical and legal applicability of SMRs. In addition, the companies will consider the possibility of joint production of such reactors. In November 2020 Rolls-Royce announced an agreement with Czech utility CEZ to assess potential deployment there, and in October 2024 CEZ acquired an approximately 20% equity stake in Rolls-Royce SMR.\n\nRolls-Royce has designed three generations of naval reactors since the 1950s and also operates a small test reactor. It led the design of a small integral reactor (SIR) of 330 MWe in the late 1980s.",
"latitude": 52.922,
"longitude": -1.476,
"newsLink1": "https://world-nuclear-news.org/articles/yokogawa-to-supply-rolls-royce-smr-control-systems ||| Yokogawa to supply Rolls-Royce SMR control systems ||| February 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/amentum-to-be-delivery-partner-for-rolls-royce-smr ||| Amentum to be delivery partner for Rolls-Royce SMR ||| January 2026",
"newsLink3": "https://www.world-nuclear-news.org/articles/rolls-royce-smr-and-ujv-rez-deepen-collaboration ||| Rolls-Royce SMR and UJV Rez deepen collaboration ||| November 2025"
},
{
"name": "RUTA-70",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 101,
"thermal": 70,
"gross": 0,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "SALUS-100",
"developer": "KAERI",
"country": "South Korea",
"hqCity": "Daejeon",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 510,
"thermal": 267,
"gross": 100,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "",
"latitude": 36.374,
"longitude": 127.377,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "SEALER-55",
"developer": "LeadCold",
"country": "Sweden",
"hqCity": "Stockholm",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 480,
"thermal": 55,
"gross": 3,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "from the Royal Institute of Technology (KTH) in Stockholm. It has a subsidiary in Canada. Its SEALER-3 (Swedish Advanced Lead Reactor) is a lead-cooled fast reactor designed with the smallest possible core that can achieve criticality in a fast spectrum using 20% enriched uranium oxide fuel. The basic reactor is 8 MWt, with a peak electric power of 3 MWe, leading to a core life of 30 full power years (at 90% availability with no refuelling) with coolant below 450°C to minimise corrosion. The company has developed novel aluminium-steel alloys that are highly corrosion-resistant in contact with liquid lead up to 450°C. The reactor vessel is designed to be small enough to permit transportation by aircraft.\nAs the regulatory framework for licensing of small reactors in Canada is better established than in most other countries, Nunavut and the Northwest Territories are likely to become the first markets for SEALER units. The Canadian Nuclear Safety Commission (CNSC) commenced phase 1 of a 15-month pre-licensing vendor design review in January 2017, but the review is now on hold at the vendor's request. In 2016 an Essel Group Middle East subsidiary agreed to invest in the Swedish-Canadian project, and in January 2017 a $200 million investment agreement was signed to license and construct \"the world's first privately funded lead-cooled nuclear power plant.” The funding will enable LeadCold to complete the pre-licensing review with the CNSC, complete a detailed engineering design of the reactor, carry out the R&D necessary for licensing the design in Canada, and construct a full-scale 3 MWe demonstration unit by about 2025. In April 2018 the company began collaboration on safety analysis with Netherlands-based NRG, which operates the Petten high-flux research reactor.\nIn February 2021 Uniper Sweden signed a joint venture agreement, creating Swedish Modular Reactors AB, with LeadCold and KTH aimed at constructing a demonstration SEALER-3 by 2030 at Oskarshamn. In February 2022 the Swedish Energy Agency awarded the joint venture funding of just over SEK 99 million ($10.6 million).\n\nSEALER-5 is a 5 MWe reactor design. Replacing the standard uranium oxide fuel with uranium nitride (UN), the same core can host 40% more fissile material. This allows the core to operate at 40% higher thermal power for the same duration as SEALER-3, i.e. 30 years.\n\nSEALER-10 is the waste management system. After 30 years of operation, the early SEALER units will be transported back to a centralised recycling facility. The plutonium and minor actinides present in the spent fuel will then be separated and converted into nitride fuel for recycle in a 10 MWe SEALER reactor. One such reactor will be sufficient to manage the used fuel of ten smaller SEALER units.",
"latitude": 59.3293,
"longitude": 18.0686,
"newsLink1": "https://www.world-nuclear-news.org/articles/swedish-partnership-for-nuclear-powered-data-centres ||| Swedish partnership for nuclear-powered data centres ||| October 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/blykalla-abb-expand-cooperation-into-maritime-applications ||| Blykalla, ABB expand cooperation into maritime applications ||| September 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/blykalla-starts-work-on-non-nuclear-prototype-smr ||| Blykalla starts work on non-nuclear prototype SMR ||| February 2025"
},
{
"name": "SHELF-M",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 310,
"thermal": 28.4,
"gross": 6.6,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "This is a Russian 6 or 10 MWe, 28 MWt integral PWR concept with turbogenerator in a cylindrical pod about 15 m long and 8 m diameter, sitting on the sea bed like Flexblue. The SHELF module uses an integral reactor with forced and natural circulation in the primary circuit, in which the core, steam generator, motor-driven circulation pump and control and protection system drive are housed in a cylindrical pressure vessel. It uses low-enriched fuel of UO2 in aluminium alloy matrix. Fuel cycle is 56 months. The reactor is based on operating prototypes, and would be serviced infrequently. It is intended as energy supply for oil and gas developments in Arctic seas, and land-based versions have been envisaged. It is at concept design stage with NIKIET which estimates that a further five years would be required in order to finalize the design, licensing, construction and commissioning. Completion of the technical design is envisaged in 2024.",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Shelf-M-project-being-developed-for-Sovinoye-gold ||| Shelf-M project being developed for Sovinoye gold deposit ||| September 2023",
"newsLink2": "https://world-nuclear-news.org/Articles/Rosatom-and-Yakutia-planning-for-SHELF-M-small-nuc ||| Rosatom and Yakutia planning for SHELF-M small nuclear plant ||| June 2022",
"newsLink3": ""
},
{
"name": "SMART",
"developer": "KAERI",
"country": "South Korea",
"hqCity": "Daejeon",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 322,
"thermal": 365,
"gross": 107,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "On a larger scale, South Korea's SMART (System-integrated Modular Advanced Reactor) is a 330 MWt pressurized water reactor with integral steam generators and advanced safety features. It is designed by the Korea Atomic Energy Research Institute (KAERI) for generating electricity (up to 100 MWe) and/or thermal applications such as seawater desalination. Design operating lifetime is 60 years, fuel enrichment 4.8%, with a three-year refuelling cycle. It has 57 fuel assemblies very similar to normal PWR ones but shorter, and it operates with a 36-month fuel cycle. All the active safety features of the original design were substituted by early 2016 with passive versions. Residual heat removal is passive. It received standard design approval (SDA) from the Korean regulator in mid-2012. A single unit can produce 90 MWe plus 40,000 m3/day of desalinated water.\n\nIn March 2015 KAERI signed an agreement with Saudi Arabia’s King Abdullah City for Atomic and Renewable Energy (KA-CARE) to assess the potential for building SMART reactors in that country, and in September 2015 further contracts were signed to that end. The cost of building the first SMART unit in Saudi Arabia was estimated at $1 billion. Through to November 2018 pre-project engineering was to be undertaken jointly including FOAK engineering design and preparations for building two units.\n\nIn April 2021 Korea Hydro & Nuclear Power (KHNP) announced that it was working with KAERI to improve the economics of the SMART design, and in September 2024 the SMART100 – an upgraded 110 MWe variant with fully passive safety systems – received standard design approval from the Korean regulator. A separate 170 MWe design, the i-SMR, is also under development for potential deployment by the late 2020s.",
"latitude": 36.374,
"longitude": 127.377,
"newsLink1": "https://www.world-nuclear-news.org/articles/korean-floating-smr-design-certified ||| Korean floating SMR design certified ||| December 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/south-korean-smr-design-approved-by-regulator ||| South Korean SMR design approved by regulator ||| September 2024",
"newsLink3": "https://world-nuclear-news.org/Articles/Hyundai,-KAERI-team-up-for-export-of-SMART-SMR ||| Hyundai, KAERI team up for export of SMART SMR ||| December 2023"
},
{
"name": "SMR-300",
"developer": "Holtec International",
"country": "USA",
"hqCity": "Camden",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 321,
"thermal": 1050,
"gross": 366,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 26.934,
"longitude": -80.094,
"newsLink1": "https://www.world-nuclear-news.org/articles/holtec-and-hyundai-ec-target-10gw-fleet-of-smrs-in-us ||| Holtec and Hyundai E&C target 10 GW SMR fleet after Palisades ||| February 2025",
"newsLink2": "https://world-nuclear-news.org/articles/holtec-signs-mou-for-smrs-in-hungary ||| Holtec signs MoU for SMRs in Hungary ||| December 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/south-yorkshire-chosen-for-holtecs-uk-smr-factory ||| South Yorkshire chosen for Holtec's proposed UK SMR factory ||| September 2024"
},
{
"name": "SSR-U",
"developer": "Moltex Energy",
"country": "United Kingdom",
"hqCity": "London",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 700,
"thermal": 40,
"gross": 16,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Moltex Energy’s Stable Salt Reactor (SSR) is a conceptual UK MSR reactor design that relies on convection from static vertical fuel tubes in the core to convey heat to the reactor coolant. Because the nuclear material is contained in fuel assemblies, standard industrial pumps can be used for the low radioactivity coolant salt. Core temperature is 500-600°C, at atmospheric pressure. Decay heat is removed by natural air convection.\n\nFuel tubes three-quarters filled with the molten fuel salt are grouped into fuel assemblies which are similar to those used in standard reactors, and use similar structural materials. The fuel salt is about 60% NaCl, 20% PuCl2, 20% UCl3, with almost any level of actinide & lanthanide trichlorides mixed in depending on the spent oxide fuel used in reprocessing – about 16% fissile overall. The individual fuel tubes are vented so that noble fission product gases escape into the coolant salt, which is a ZrF4-KF-NaF mixture, the radionuclide accumulation of which is managed. Iodine and caesium stay dissolved in the fuel salt. Other fission product gases condense on the upper fuel tube walls and fall back into the fuel mixture before they can escape into the coolant. The fuel assemblies can be moved laterally without removing them. Refuelling is thus continuous online, and after the fuel is sufficiently burned up the depleted assemblies are stored at one side of the pool for a month to cool, then lifted out so that the salt freezes. Reprocessing is straightforward, and any level of lanthanides can be handled.\n\nSSR factory-produced modules are 150 MWe containing fuel, pumps, primary heat exchanger, control blades and instrumentation. Several, up to gigawatt-scale, can share a reactor tank, half-filled with the coolant salt which transfers heat away from the fuel assemblies to the peripheral steam generators, essentially by convection, at atmospheric pressure. There are three variants of the SSR: the Stable Salt Reactor – Wasteburner (SSR-W) fast reactor; about two years behind developmentally, the SSR-U thermal-spectrum reactor for a variety of applications; and the SSR-Th with thorium fuel. The GridReserve version has heat storage.\n\nThe SSR-W is the simplest and cheapest, due to compact core and no moderator. The primary fissile fuel in this original fast reactor version was to be plutonium-239 chloride with minor actinides and lanthanides, recovered from LWR fuel or from an SSR-U reactor. In 2020 the SSR-W fuel was 25% reactor-grade PuCl3 with 30% UCl3 and 45% KCl. Primary coolant salt is ZrF4-KF at a maximum temperature of 590°C. Secondary coolant is nitrate salt buffer. Burn-up is 120-200 GWd/t. A 750 MWt/300 MWe demonstration plant is envisaged, the SSR-W300. An agreement has been signed with New Brunswick Power for initial deployment at Point Lepreau in Canada and in March 2021 the Canadian government announced a C$50.5 million investment towards this. In April 2021 plans were confirmed for this plus a plant for recycling used Canadian nuclear fuel for it. In November 2020 the two companies were joined by ARC Canada in setting up an SMR vendor cluster there. The Canadian Nuclear Safety Commission pre-licensing vendor design review of the SSR-W has completed the first phase. The first operating reactor is envisaged after 2030.\n\nThe company has announced the physically larger and more expensive SSR-U ‘global workhorse version’ of its design, with a thermal neutron spectrum running on LEU fluorides (up to 7% enriched) with graphite built into the fuel assemblies, which increases the size of the core. It runs at a higher temperature than the fast version – minimum 600°C – with ZrF4-NaF coolant salt stabilized with ZrF2. As well as electricity, hydrogen production is its purpose. It is designed to be compatible with thorium breeding to U-233. It is seen as having a much larger potential market, and initial deployment in the UK in the 2030s is anticipated, with potential for replacing CCGT and coal plants.\n\nThe SSR-Th is a thorium breeder version of the SSR-U, with thorium in the coolant salt and the U-233 produced is progressively dissolved in bismuth at the bottom of the salt pool. This contains U-238 to denature it and ensure there is never a proliferation risk. Once the desired level of U-233 is achieved (under 20%), the bismuth with uranium is taken out batch-wise, and the mixed-isotope uranium is chlorinated to become fuel. If the fuel is used in a fast reactor, plutonium and actinides can be added.\n\nMoltex has also put forward its GridReserve molten nitrate salt heat storage concept to enable the reactor to supplement intermittent renewables.",
"latitude": 45.273,
"longitude": -66.063,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "SSTAR",
"developer": "ANL",
"country": "USA",
"hqCity": "Argonne",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 500,
"thermal": 45,
"gross": 20,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The Secure Transportable Autonomous Reactor (STAR) project at Argonne National Laboratory was developing small, multi-purpose systems that operate nearly autonomously for the very long term. The STAR-LM is a factory-fabricated fast neutron modular reactor design cooled by lead-bismuth eutectic, with passive safety features. Its 300-400 MWt size means it can be shipped by rail. It uses uranium-transuranic nitride fuel in a 2.5 m diameter cartridge which is replaced every 15 years. Decay heat removal is by external air circulation. The STAR-LM was conceived for power generation with a capacity of about 175 MWe.\n\nThe STAR-H2 is an adaptation of the same reactor for hydrogen production, with reactor heat at up to 800°C being conveyed by a helium circuit to drive a separate thermochemical hydrogen production plant, while lower grade heat is harnessed for desalination (multi-stage flash process). Its development is further off.\n\nA smaller STAR variant is the Small Sealed Transportable Autonomous Reactor (SSTAR) which was being developed by Lawrence Livermore, Argonne and Los Alamos National Laboratories in collaboration with others including Toshiba. It has lead or Pb-Bi cooling, 564°C core outlet temperature and has integral steam generator inside the sealed unit, which would be installed below ground level. Conceived in sizes 10-100 MWe, main development was focused on a 45 MWt/20 MWe version as part of the US Generation IV effort. After a 20- or 30-year operating lifetime without refuelling, the whole reactor unit is then returned for recycling the fuel. The reactor vessel is 12 metres high and 3.2 m diameter and the core one metre high and 1.2 m diameter (20 MWe version). SSTAR would eventually be coupled to a Brayton cycle turbine using supercritical carbon dioxide with natural circulation to four heat exchangers. A prototype was envisaged for 2015, but development has apparently ceased.",
"latitude": 41.713,
"longitude": -87.982,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "STAR",
"developer": "ANL",
"country": "USA",
"hqCity": "Argonne",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 300,
"thermal": 30,
"gross": 10,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The Secure Transportable Autonomous Reactor (STAR) project at Argonne National Laboratory was developing small, multi-purpose systems that operate nearly autonomously for the very long term. The STAR-LM is a factory-fabricated fast neutron modular reactor design cooled by lead-bismuth eutectic, with passive safety features. Its 300-400 MWt size means it can be shipped by rail. It uses uranium-transuranic nitride fuel in a 2.5 m diameter cartridge which is replaced every 15 years. Decay heat removal is by external air circulation. The STAR-LM was conceived for power generation with a capacity of about 175 MWe.\n\nThe STAR-H2 is an adaptation of the same reactor for hydrogen production, with reactor heat at up to 800°C being conveyed by a helium circuit to drive a separate thermochemical hydrogen production plant, while lower grade heat is harnessed for desalination (multi-stage flash process). Its development is further off.\n\nA smaller STAR variant is the Small Sealed Transportable Autonomous Reactor (SSTAR) which was being developed by Lawrence Livermore, Argonne and Los Alamos National Laboratories in collaboration with others including Toshiba. It has lead or Pb-Bi cooling, 564°C core outlet temperature and has integral steam generator inside the sealed unit, which would be installed below ground level. Conceived in sizes 10-100 MWe, main development was focused on a 45 MWt/20 MWe version as part of the US Generation IV effort. After a 20- or 30-year operating lifetime without refuelling, the whole reactor unit is then returned for recycling the fuel. The reactor vessel is 12 metres high and 3.2 m diameter and the core one metre high and 1.2 m diameter (20 MWe version). SSTAR would eventually be coupled to a Brayton cycle turbine using supercritical carbon dioxide with natural circulation to four heat exchangers. A prototype was envisaged for 2015, but development has apparently ceased.",
"latitude": 41.713,
"longitude": -87.982,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Starcore",
"developer": "Starcore Nuclear",
"country": "Canada",
"hqCity": "Montreal",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 35,
"gross": 14,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "This is a small (20 MWe) concept design of helium-cooled reactor from StarCore Nuclear in Quebec, designed for remote locations (displacing diesel and propane) and with remote control system via satellite. It is expandable to 100 MWe. The units would be installed below grade and in pairs. They are truck-transportable, with reactor vessels 2.5 m diameter and 6 m high. Fuel is TRISO in carbon prismatic matrix. Each reactor has a five-year refuelling schedule. The secondary cooling circuit is nitrogen, to a steam generator driving a turbine. The company offers a build-own-operate-decommission concept with a power purchase agreement for the life of the reactor, mentioning C$0.18 per kWh. The units are designed to deliver both electricity and potable water.\n\nThe company has applied to the CNSC to start the pre-licensing vendor design review process. \n\nIn April 2018, Canadian Nuclear Laboratories (CNL) launched its SMR review – a separate process to licensing – with a view to having an SMR constructed on its Chalk River site by 2026. In February 2019 CNL announced that StarCore had completed the prequalification stage and been invited to enter the due diligence stage.",
"latitude": 45.4215,
"longitude": -75.6972,
"newsLink1": "https://www.world-nuclear-news.org/Articles/CNL-selects-first-SMR-vendors-for-cost-shared-fund ||| CNL selects first SMR vendors for cost-shared funding ||| November 2019",
"newsLink2": "https://www.world-nuclear-news.org/Articles/SMR-proposals-progress-through-Canadian-process ||| SMR proposals progress through Canadian process ||| February 2019",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Canadian-design-review-for-StarCore-HTGR ||| Canadian design review for StarCore HTGR ||| November 2016"
},
{
"name": "STAR-H2",
"developer": "ANL",
"country": "USA",
"hqCity": "Argonne",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 850,
"thermal": 400,
"gross": 175,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "The Secure Transportable Autonomous Reactor (STAR) project at Argonne National Laboratory was developing small, multi-purpose systems that operate nearly autonomously for the very long term. The STAR-LM is a factory-fabricated fast neutron modular reactor design cooled by lead-bismuth eutectic, with passive safety features. Its 300-400 MWt size means it can be shipped by rail. It uses uranium-transuranic nitride fuel in a 2.5 m diameter cartridge which is replaced every 15 years. Decay heat removal is by external air circulation. The STAR-LM was conceived for power generation with a capacity of about 175 MWe.\n\nThe STAR-H2 is an adaptation of the same reactor for hydrogen production, with reactor heat at up to 800°C being conveyed by a helium circuit to drive a separate thermochemical hydrogen production plant, while lower grade heat is harnessed for desalination (multi-stage flash process). Its development is further off.\n\nA smaller STAR variant is the Small Sealed Transportable Autonomous Reactor (SSTAR) which was being developed by Lawrence Livermore, Argonne and Los Alamos National Laboratories in collaboration with others including Toshiba. It has lead or Pb-Bi cooling, 564°C core outlet temperature and has integral steam generator inside the sealed unit, which would be installed below ground level. Conceived in sizes 10-100 MWe, main development was focused on a 45 MWt/20 MWe version as part of the US Generation IV effort. After a 20- or 30-year operating lifetime without refuelling, the whole reactor unit is then returned for recycling the fuel. The reactor vessel is 12 metres high and 3.2 m diameter and the core one metre high and 1.2 m diameter (20 MWe version). SSTAR would eventually be coupled to a Brayton cycle turbine using supercritical carbon dioxide with natural circulation to four heat exchangers. A prototype was envisaged for 2015, but development has apparently ceased.",
"latitude": 41.713,
"longitude": -87.982,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "STAR-LM",
"developer": "ANL",
"country": "USA",
"hqCity": "Argonne",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 550,
"thermal": 180,
"gross": 100,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "The Secure Transportable Autonomous Reactor (STAR) project at Argonne National Laboratory was developing small, multi-purpose systems that operate nearly autonomously for the very long term. The STAR-LM is a factory-fabricated fast neutron modular reactor design cooled by lead-bismuth eutectic, with passive safety features. Its 300-400 MWt size means it can be shipped by rail. It uses uranium-transuranic nitride fuel in a 2.5 m diameter cartridge which is replaced every 15 years. Decay heat removal is by external air circulation. The STAR-LM was conceived for power generation with a capacity of about 175 MWe.\n\nThe STAR-H2 is an adaptation of the same reactor for hydrogen production, with reactor heat at up to 800°C being conveyed by a helium circuit to drive a separate thermochemical hydrogen production plant, while lower grade heat is harnessed for desalination (multi-stage flash process). Its development is further off.\n\nA smaller STAR variant is the Small Sealed Transportable Autonomous Reactor (SSTAR) which was being developed by Lawrence Livermore, Argonne and Los Alamos National Laboratories in collaboration with others including Toshiba. It has lead or Pb-Bi cooling, 564°C core outlet temperature and has integral steam generator inside the sealed unit, which would be installed below ground level. Conceived in sizes 10-100 MWe, main development was focused on a 45 MWt/20 MWe version as part of the US Generation IV effort. After a 20- or 30-year operating lifetime without refuelling, the whole reactor unit is then returned for recycling the fuel. The reactor vessel is 12 metres high and 3.2 m diameter and the core one metre high and 1.2 m diameter (20 MWe version). SSTAR would eventually be coupled to a Brayton cycle turbine using supercritical carbon dioxide with natural circulation to four heat exchangers. A prototype was envisaged for 2015, but development has apparently ceased.",
"latitude": 41.713,
"longitude": -87.982,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "START",
"developer": "Transmutex",
"country": "Switzerland",
"hqCity": "Geneva",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 450,
"thermal": 600,
"gross": 220,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 46.2209062981948,
"longitude": 6.09867063048406,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Stellarium",
"developer": "Stellaria",
"country": "France",
"hqCity": "Grenoble",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 750,
"thermal": 540,
"gross": 250,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "",
"latitude": 45.1919935401998,
"longitude": 5.70655652732785,
"newsLink1": "https://www.world-nuclear-news.org/articles/stellaria-seeks-permission-to-build-experimental-reactor ||| Stellaria seeks permission to build experimental reactor ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/equinix-signs-up-for-power-from-first-stellaria-reactor ||| Equinix signs up for power from first Stellaria reactor ||| November 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/equinix-signs-further-agreements-with-smr-developers ||| Equinix signs further agreements with SMR developers ||| August 2025"
},
{
"name": "SVBR-100",
"developer": "AKME-Engineering",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 495,
"thermal": 280,
"gross": 100,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "A smaller and newer Russian design as a small modular reactor was to be the lead-bismuth fast reactor (SVBR) of 280 MWt, 100 MWe, being developed by AKME-engineering and involving Gidropress in the design. It is an integral design, with 12 steam generators and two main circulation pumps sitting in the same Pb-Bi pool at 340-490°C as the reactor core. It is designed to be able to use a wide variety of fuels, though the pilot unit would initially use uranium oxide enriched to 16.3%. With U-Pu MOX fuel it would operate in closed cycle. Refuelling interval would be 7-8 years and 60-year operating lifetime was envisaged. The melting point of the Pb-Bi coolant is 123.5°C, so it is readily kept molten during shutdown by decay heat supplemented by external heat sources if required.\nThe SVBR-100 unit of 280 MWt would be factory-made and transported (railway, road or waterway) as a 4.5m diameter, 8.2m high module. A power station with such modules was expected to supply electricity at lower cost than any other new technology with an equal capacity as well as achieving inherent safety and high proliferation resistance. (Russia built seven Alfa-class submarines, each powered by a compact 155 MWt Pb-Bi cooled reactor, and 80 reactor-years' operational experience was acquired with these.) In October 2015 Rosatom reported: \"Experts have confirmed there are no scientific or technical issues that would prevent completion of the project and obtaining a construction licence.\" Then in November 2016 Rosatom said it expected to work out the main specifications for construction of the SVBR-100 by mid-2017, but in 2018 the project was dropped. Overnight capital cost was earlier estimated as $4000-4500/kW and generating costs 4-5 c/kWh on 90% load factor.\n\nIn December 2009, AKME-engineering, a 50-50 joint venture, was set up by Rosatom and the En+ Group (a subsidiary of Basic Element Group) as an open joint stock company to develop and build a pilot SVBR unit14. En+ is an associate of JSC EuroSibEnergo and a 53.8% owner of Rusal, which had been in discussion with Rosatom regarding a Far East nuclear power plant and Phase II of the Balakovo nuclear plant. It was to contribute most of the capital, and Rosatom is now looking for another investor. In 2011 the EuroSibEnergo 50% share passed to its subsidiary JSC Irkutskenergo. The main project participants are OKB Gidropress at Podolsk, VNIPIET OAO at St Petersburg, and the RF State Research Centre Institute of Physics & Power Engineering (IPPE or FEI) at Obninsk.\n\nThe plan was to complete the design development and put online a 100 MWe pilot facility by 2019, with total investment of RUR36 billion ($550 million). The site was to be the Research Institute of Atomic Reactors (RIAR or NIIAR) at Dimitrovgrad – Russia's largest nuclear research centre – though earlier plans were to put it at IPPE/FEI at Obninsk. The SVBR-100 would have been the first reactor cooled by heavy metal to generate electricity. It is described by Gidropress as a multi-function reactor for power, heat or desalination.\n\nAn SVBR-10 was also envisaged, with the same design principles, a 20-year refuelling interval and generating capacity of 12 MWe, and it too is a multi-purpose unit.",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Land-secured-for-pilot-fast-reactor ||| Land secured for pilot fast reactor ||| June 2013",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Fast-reactor-developer-licensed-to-build ||| Fast reactor developer licensed to build ||| May 2013",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Small-fast-reactor-simulator-commissioned ||| Small fast reactor simulator commissioned ||| March 2013"
},
{
"name": "TEPLATOR",
"developer": "UWB & CIIRC CTU",
"country": "Czech Republic",
"hqCity": "Prague",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 180,
"thermal": 50,
"gross": 0,
"fuelEnrichment": "<5^%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 50.0839243681424,
"longitude": 14.428387394614,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Thorcon TMSR",
"developer": "ThorCon",
"country": "USA",
"hqCity": "Stevenson",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 557,
"gross": 250,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "Martingale in the USA is designing the ThorCon MSR (TMSR), which is a 250 MWe scaled-up Oak Ridge MSRE. It is a single-fluid thorium converter reactor in the thermal spectrum, graphite moderated. It uses a combination of U-233 from thorium and low-enriched U-235 (19.7% enriched) from mined uranium. Fuel salt is sodium-beryllium fluoride (BeF2-NaF) with dissolved uranium and thorium tetrafluorides (Li-7 fluoride is avoided for cost reasons). Secondary loop coolant salt is also sodium-beryllium fluoride. It operates at 700°C. There is no online processing – this takes place in a centralized plant at the end of the core life – with off-gassing of some fission products meanwhile.\n\nSeveral 550 MWt, 250 MWe TMSR modules would comprise a power station. Each module contains two replaceable reactors in sealed 'cans'. Each can contains a reactor ‘pot’, a primary heat exchanger and a primary loop pump. Each can is 11.6m high, 7.3m diameter and weighs 360 tonnes. The cans sit in silos below grade (30 m down). Below each is a 32-cylinder fuel salt drain tank, under a freeze valve.\nAt any one time, just one of the cans of each module is producing power. The other can is in cool-down mode. Every four years the can that has been cooling is removed and replaced with a new can. The fuel salt is transferred to the new can, and the can that has been operating goes into cool-down mode. In October 2015 Martingale signed an agreement with three Indonesian companies to commission a 500 MW ThorCon plant (TMSR-500) there. In 2020 Thorcon International was working with South Korea’s Daewoo Shipbuilding and Marine Engineering to build the TMSR500 as the first nuclear power plant (PLTN) in Indonesia.\n\nIn July 2020 Thorcon International signed a cooperation agreement with Indonesia’s Defence Ministry to evaluate developing a small TMSR (under 50 MW) for either power generation or marine propulsion. Thorcon will provide technical support for the ministry’s R&D.",
"latitude": 1.3521,
"longitude": 103.8198,
"newsLink1": "https://www.world-nuclear-news.org/articles/regulatory-approval-for-indonesian-site-survey ||| Regulatory approval for Indonesian site survey ||| August 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/thorcon-applies-to-build-indonesias-first-nuclear-power-plant ||| Thorcon applies to build Indonesia's first nuclear power plant ||| March 2025",
"newsLink3": "https://www.world-nuclear-news.org/Articles/ThorCon-begins-pre-licensing-consultation-in-Indon ||| ThorCon begins pre-licensing consultation in Indonesia ||| April 2023"
},
{
"name": "THORIZON",
"developer": "Thorizon",
"country": "Netherlands",
"hqCity": "Amsterdam",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 550,
"thermal": 250,
"gross": 100,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "",
"latitude": 52.3676,
"longitude": 4.9041,
"newsLink1": "https://www.world-nuclear-news.org/articles/dutch-support-for-msr-demonstrator-facility ||| Dutch support for molten salt reactor demonstrator facility ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/thorizon-partners-with-molten-salt-energy-storage-provider ||| Thorizon partners with molten salt energy storage provider ||| April 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/new-funding-to-advance-thorizon-molten-salt-reactor-development ||| New funding to advance Thorizon molten salt reactor development ||| March 2025"
},
{
"name": "TMSR-SF",
"developer": "Shanghai Institute of Applied Physics",
"country": "China",
"hqCity": "Shanghai",
"reactorType": "Molten salt cooled",
"spectrum": "Thermal",
"outletTemp": 650,
"thermal": 10,
"gross": 2,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "China is planning a 10 MWe thorium-breeding molten-salt reactor (Th-MSR or TMSR), essentially an LFTR, with 2025 target for operation at the Shanghai Institute of Nuclear Applied Physics (SINAP, under the China Academy of Sciences). This is also known as the fluoride salt-cooled high-temperature reactor (FHR). It has low-enriched TRISO fuel as pebble bed, FLiBe primary coolant at 650°C and FLiNaK secondary coolant. A 100 MWt demonstration pebble-bed plant with open fuel cycle is planned by about 2025. SINAP sees this design having potential for higher temperatures than MSRs with fuel salt.\n\nChina claims to have the world's largest national effort on these and hopes to obtain full intellectual property rights on the technology. The US Department of Energy is collaborating with the China Academy of Sciences on the programme, which had a start-up budget of $350 million. ",
"latitude": 31.204,
"longitude": 121.432,
"newsLink1": "https://www.world-nuclear-news.org/articles/chinese-msr-achieves-conversion-of-thorium-uranium-fuel ||| Chinese molten salt reactor achieves conversion of thorium-uranium fuel ||| November 2025",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Operating-permit-issued-for-Chinese-molten-salt-re ||| Operating permit issued for Chinese molten salt reactor ||| June 2023",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Chinese-molten-salt-reactor-cleared-for-start-up ||| Chinese molten-salt reactor cleared for start up ||| August 2022"
},
{
"name": "U-Battery",
"developer": "Urenco",
"country": "United Kingdom",
"hqCity": "Stoke Poges",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 10,
"gross": 4,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "Urenco with others commissioned a study by TU-Delft and Manchester University on the basis of which it has called for European development of a very small 'plug and play' inherently-safe reactor called the U-Battery. This is based on graphite-moderated, helium cooled HTR concepts such as the UK's Dragon reactor (to 1975). The fuel block design is based on that of the Fort St Vrain reactor in the USA. It would use TRISO fuel with 17-20% enriched uranium and possibly thorium with a beryllium oxide reflector. The 10 MWt design can produce 750°C process heat or up to 4 MWe back-up and off-grid power. The consortium envisages up to six U-Batteries at one site.\nThis micro-SMR U-battery would run for five years before refuelling and servicing, a larger 20 MWt one would run for 10 years. The 10 MWt/4 MWe design, 1.8 m diameter, may be capable of being returned to the factory for refuelling. The U-Battery consortium, led by Urenco, has gained UK government support for a prototype, with target operation in 2028. Wood, Laing O’Rourke, Cammell Laird and Kinectrics are involved.\n\nIn mid-2018 the consortium was one of eight organisations to be awarded a contract to produce a feasibility study as part of the UK government's Advanced Modular Reactor Feasibility and Development project, and in July 2020 it was selected for phase 2 of this. It has been accepted for pre-licensing vendor design review with the Canadian Nuclear Safety Commission (CNSC), from 2017. In July 2019 it became the first design to complete the first of the four phases of Canadian Nuclear Laboratories’ review process for siting an SMR at Chalk River Laboratories in Ontario.\n\nIn March 2023 Urenco announced that it planned to cease supporting the development of its U-Battery advanced modular reactor project as it had exhausted attempts to secure the commitment of new commercial investors. Urenco said it would transfer the intellectual property to the UK's National Nuclear Laboratory.",
"latitude": 51.544,
"longitude": -0.604,
"newsLink1": "https://www.world-nuclear-news.org/Articles/Urenco-exits-U-Battery-micro-reactor-project ||| Urenco exits U-Battery micro-reactor project ||| March 2023",
"newsLink2": "https://www.world-nuclear-news.org/Articles/U-Battery-unveils-full-scale-SMR-mock-up ||| U-Battery unveils full-scale SMR mock-up ||| September 2021",
"newsLink3": "https://www.world-nuclear-news.org/Articles/U-Battery-SMR-moves-to-next-stage-of-Canadian-asse ||| U-Battery SMR moves to next stage of Canadian assessment ||| July 2019"
},
{
"name": "UNITHERM",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 330,
"thermal": 30,
"gross": 6.6,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": false,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "This is an integral 30 MWt, 6.6 MWe PWR conceptual design from Russia’s Research and Development Institute of Power Engineering (RDIPE or NIKIET). It has three coolant loops, with natural circulation, and claims self-regulation with burnable poisons in unusual metal-ceramic fuel design, so needs no more than an annual maintenance campaign and no refueling during a 25-year life. The mass of one unit with shielding is 180 tonnes, so it can be shipped complete from the factory to site.",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "VBER-300",
"developer": "OKBM Afrikantov",
"country": "Russia",
"hqCity": "Nizhny Novgorod",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 328,
"thermal": 917,
"gross": 325,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "A larger Russian factory-built and barge-mounted unit (requiring a 12,000 tonne vessel) is the VBER-150, of 350 MWt, 110 MWe. It is modular and is derived by OKBM from naval designs, with two steam generators. Uranium oxide fuel enriched to 4.7% has burnable poison; it has low burn-up (31 GWd/t average, 41.6 GWd/t maximum) and eight-year refuelling interval.\n\nOKBM Afrikantov's larger VBER-300 PWR is a 917 MWt, 325 MWe unit, the first of which is planned to be built in Kazakhstan. It was originally envisaged in pairs as a floating nuclear power plant, displacing 49,000 tonnes. As a cogeneration plant it is rated at 200 MWe and 1900 GJ/hr. The reactor is designed for 60-year life and 90% capacity factor. It has four external steam generators and a cassette core with 85 standard VVER fuel assemblies enriched to 4.95% and 50 GWd/tU burn-up with a 72-month fuel cycle. Versions with three and two steam generators are also envisaged, of 230 and 150 MWe respectively. Also, with more sophisticated and higher-enriched (18%) fuel in the core, the refuelling interval can be pushed from two years out to five years (6 to 15 years fuel cycle) with burn-up to 125 GWd/tU. A 2006 joint venture between Atomstroyexport and Kazatomprom set this up for development as a basic power source in Kazakhstan, then for exporte. It is also envisaged for use in Russia, mainly as cogeneration unit. It is considered likely for near-term deployment.\n\nThe company also offers 200-600 MWe designs based on a standard 100 MWe module and explicitly based on naval units.",
"latitude": 56.3269,
"longitude": 44.0059,
"newsLink1": "https://world-nuclear-news.org/Articles/Primorsky-named-as-possible-nuclear-power-plant-lo ||| Primorsky named as possible nuclear power plant location ||| October 2021",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Nuclear-power-plans-for-Kazakhstan-firm-up ||| Nuclear power plans for Kazakhstan firm up ||| November 2007",
"newsLink3": ""
},
{
"name": "VK-300",
"developer": "NIKIET",
"country": "Russia",
"hqCity": "Moscow",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 280,
"thermal": 750,
"gross": 250,
"fuelEnrichment": "<5%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "Another larger Russian reactor with completed detailed design is NIKIET’s VK-300 integral boiling water reactor of 750 MWt, 250 MWe, being developed specifically for cogeneration of both power and district heating or heat for desalination (150 MWe plus 1675 GJ/hr) by the N.A. Dollezhal Research and Development Institute of Power Engineering (RDIPE or NIKIET) together with several major research and engineering institutes. It has evolved from the 50 MWe (net) VK-50 BWR at Dimitrovgradf, but uses standard components wherever possible, and has 313 fuel elements similar to the VVER. Cooling is passive, by convection, and all safety systems are passive. Fuel enrichment is 4% and burn-up is 41 GWd/tU with a 72-month refuelling interval. It is capable of producing 250 MWe if solely electrical. Design operating lifetime is 60 years.\n\nIn September 2007 it was announced that six would be built at Kola or Archangelsk and at Primorskaya in the far east, to start operating 2017-20,4 but no more has been heard of this plan. A feasibility study was undertaken for Arkhangelsk nuclear cogeneration plant with four units. As a cogeneration plant it was intended for the Mining & Chemical Combine at Zheleznogorsk, but MCC is reported to prefer the VBER-300. The design was completed in 2013.",
"latitude": 55.751,
"longitude": 37.618,
"newsLink1": "",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Westinghouse LFR",
"developer": "Westinghouse",
"country": "USA",
"hqCity": "Cranberry Township",
"reactorType": "Metal-cooled",
"spectrum": "Fast",
"outletTemp": 500,
"thermal": 1200,
"gross": 450,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": false,
"notes": "The Westinghouse Lead-cooled Fast Reactor (LFR) programme originated from an investigation performed in 2015 aimed at identifying the technology that would best support addressing the challenges of nuclear power, for global deployment. It is at the conceptual design stage for up to 450 MWe as a modular pool-type unit, simple, scalable and with passive safety. It will have flexible output to complement intermittent renewable feed to the grid. Its high temperature – eventually 650°C – capabilities will allow industrial heat applications. Westinghouse expects it to be very competitive, having low capital and construction costs with enhanced safety.\n\nBecause lead coolant operates at atmospheric pressure and does not exothermically react with air or with power conversion fluids (such as supercritical carbon dioxide and water), LFR technology also eliminates the need and associated expense of extra components and redundant safety systems required by other plant designs for protection against coolant leakages. Further operational and safety enhancements are also achieved by adoption of a fuel/cladding combination with high temperature capability based on those under development by Westinghouse in the accident tolerant fuel programme.\n\nIn February 2017 the company signed an agreement with the Italian National Agency for New Technologies, Energy and Sustainable Economic Development (ENEA) and Ansaldo Nucleare to develop the design. The development also involves several UK companies and initial licensing is envisaged with the UK Office for Nuclear Regulation (ONR). In April 2021 an Ansaldo subsidiary was contracted to design, provide, install and test key components of the reactor at the Versatile Lead Loop Facility and Passive Heat Removal Facility, which are to be designed and installed at Ansaldo Nuclear's site in Wolverhampton in the UK. A prototype LFR will be about 300 MWe, running at 500 °C.\n\nBeyond base-load electricity generation, the high-temperature operation of the LFR will allow for effective load-following capability enabled by an innovative thermal energy storage system, as well as delivery of process heat for industrial applications and water desalination. A supercritical carbon dioxide power conversion system that uses air as the ultimate heat sink significantly reduces water utilization and eliminates the need for siting the plant near large water bodies.",
"latitude": 40.685,
"longitude": -80.107,
"newsLink1": "https://www.world-nuclear-news.org/articles/consortium-to-speed-up-development-of-lead-cooled ||| Consortium to speed up development of lead-cooled SMRs ||| November 2023",
"newsLink2": "https://www.world-nuclear-news.org/Articles/Westinghouse,-Ansaldo-progress-with-LFR-developmen ||| Westinghouse, Ansaldo progress with LFR development ||| May 2023",
"newsLink3": "https://www.world-nuclear-news.org/Articles/Westinghouse-and-Ansaldo-Nucleare-collaborate-on-n ||| Westinghouse and Ansaldo Nucleare collaborate on next-gen LFR nuclear plant ||| October 2022"
},
{
"name": "XAMR",
"developer": "Naarea",
"country": "France",
"hqCity": "Nanterre",
"reactorType": "Molten salt cooled",
"spectrum": "Fast",
"outletTemp": 625,
"thermal": 80,
"gross": 40,
"fuelEnrichment": "NA",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "Naarea is developing the XAMR, a molten salt fast neutron microreactor capable of producing 40 MWe of electricity/80 MWt of heat that will burn plutonium and by reusing long-lived nuclear waste help close the fuel cycle.\n\nThe XAMR uses sodium chloride (NaCl), in which actinides in the form of plutonium chloride and uranium chloride are dissolved. In the absence of an industrial sector to supply fuel for these innovative technologies, the synthesis of fuel salt is a key step for validating the project's feasibility. This involves developing a reproducible synthesis method to produce a pure fuel salt containing fissile materials.\n\nSince 2024, through its joint laboratory – the Innovation Molten Salt Lab (IMSLab) – with the French National Centre for Scientific Research (CNRS) and Paris-Saclay University, Naarea has been working with the European Commission's Joint Research Centre (JRC) on the synthesis of NaCl-PuCl3 salt.\n\nThe focus of this collaboration is on validating a proliferation-resistant method of synthesizing NaCl-PuCl3 salt from plutonium oxide (PuO2), via a pyrochemical process, as well as experimentally determining fundamental data related to this fuel. This strategic method, proposed by Naarea, is based on a process that involves bubbling gas through a mixture of NaCl and PuO2, brought to a high temperature. This process is implemented thanks to specific experimental equipment developed and operated by the JRC.",
"latitude": 48.9010278842398,
"longitude": 2.21432732872143,
"newsLink1": "https://www.world-nuclear-news.org/articles/naarea-advances-development-of-molten-salt-reactor-fuel ||| Naarea advances development of molten salt reactor fuel ||| September 2025",
"newsLink2": "https://www.world-nuclear-news.org/articles/naarea-opens-test-facility-for-microreactor-development ||| Naarea opens test facility for microreactor development ||| February 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/phoenix-manufacture-to-help-industrialise-xamr ||| Phoenix Manufacture to help industrialise XAMR ||| January 2025"
},
{
"name": "Xe-100",
"developer": "X-energy",
"country": "USA",
"hqCity": "Rockville",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 200,
"gross": 80,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "200 MWt, 80 MWe, and has been in talks with utilities, stressing that a plant will fit on a 4 ha site, below grade for electricity and/or process heat. The initial TRISO fuel in the mid-2020s will utilize uranium oxycarbide (UCO) made from high-assay low-enriched uranium (HALEU), but longer-term thorium is intended as the primary fuel. Unlike other pebble bed HTRs, the fuel will only pass through once, with high 160 GWd/t burn-up. Fairly rapid load-following from 25% to 100% is a feature of the helium-cooled design running at 750 °C. Factory-made units with 60-year operational life would be transported to the site by road and installed.\n\nThe company has been in discussion with several utilities, including South Carolina Electricity & Gas (SCEG), regarding replacing coal-fired capacity with the four-pack installations. Industrial process heat is also a likely application. X-energy is working in partnership with BWX Technology, Oregon State University, Teledyne-Brown Engineering, SGL Group, Idaho National Laboratory (INL), and Oak Ridge National Laboratory (ORNL) on the design. In January 2016 the US DOE awarded a Gateway for Accelerated Innovation in Nuclear (GAIN) grant to the project, worth $53 million. In September 2016 Burns & McDonnell Engineering joined the project as architectural and engineering partner, in parallel with the DOE five-year award. The Xe-100 is a candidate for the US Advanced Reactor Demonstration Program (ARDP). In 2020 the Xe-100 received an initial grant of $80 million under the programme. In March 2025 Dow submitted a construction permit application to the NRC for an Xe-100 plant at the Long Mott, Texas site for industrial process heat. In October 2024 Amazon partnered with Energy Northwest for a ‘Cascade’ multi-reactor Xe-100 facility in Washington state.\n\nIn April 2021 X-energy signed an agreement with Energy Northwest and a public utility to set up the Tri Energy Partnership with a view to building an Xe-100 plant near the Columbia nuclear power plant in Washington state. The $2.4 billion project would be half funded by the ARDP and take seven years. In July 2023 Energy Northwest and X-energy signed a joint development agreement for the deployment of up to 12 Xe-100s in central Washington state.\n\nIn November 2017 the company signed an agreement with Jordan Atomic Energy Commission to consider building the Xe-100 in Jordan. In August 2020 the company initiated a vendor design review with the Canadian Nuclear Safety Commission. Kinetrics is leading X-energy’s Canadian regulatory affairs and licensing efforts. X-energy is targeting initial deployment in the late 2020s.\n\nIn August 2016 X-energy signed an agreement to work with Southern Nuclear Operating Company to collaborate on development and commercialization of their respective small reactor designs. Southern is developing an MSR, the Molten Chloride Fast Reactor (MCFR). In September 2018, X-energy said that its design was about 50% complete, and that it hoped the full design would be finalized by 2022 or 2023.\n\nX-energy has a TRISO pilot fuel fabrication facility at Oak Ridge National Laboratory, Tennessee and in November 2019 it agreed with Global Nuclear Fuel (GNF) to set up commercial HALEU TRISO production at GNF's Wilmington plant. X-energy's TRISO-X subsidiary received an NRC licence for HALEU fuel fabrication in February 2026. X-energy also has agreements with Centrus Energy in the USA to develop TRISO fabrication technology for uranium carbide fuel, and with NFI at Tokai in Japan, where NFI has 400 kgU/yr HTR fuel capacity.",
"latitude": 39.0837,
"longitude": -77.1503,
"newsLink1": "https://www.world-nuclear-news.org/articles/long-term-agreement-strengthens-x-energy-graphite-supply-chain ||| Long-term graphite agreement strengthens X-energy supply chain ||| January 2026",
"newsLink2": "https://www.world-nuclear-news.org/articles/amazon-updates-smr-progress-with-new-images-of-proposed-plant ||| Amazon updates SMR progress, with new images of proposed plant ||| October 2025",
"newsLink3": "https://www.world-nuclear-news.org/articles/study-confirms-feasibility-of-xe-100-smr-for-alberta ||| Study confirms feasibility of Xe-100 SMR for Alberta ||| September 2025"
},
{
"name": "XENITH",
"developer": "X-energy",
"country": "USA",
"hqCity": "Rockville",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 750,
"thermal": 20,
"gross": 5,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": false,
"notes": "In March 2020 the US Department of Defense awarded a $14.3 million contract for further development of the design as a microreactor under 5 MWe – the Xe-Mobile, with all components housed in a standard shipping container. It is to be able to operate at full power – at least 1 MWe – for at least three years. In March 2021 the DOD selected this as one of two candidates to proceed to final engineering design in 2022 under the $30 million second phase of the Project Pele programme (see Military developments section above).",
"latitude": 39.0837,
"longitude": -77.1503,
"newsLink1": "https://www.world-nuclear-news.org/articles/x-energy-military-to-advance-microreactor-technology ||| X-energy, military to advance microreactor technology ||| August 2025",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Halo 10",
"developer": "Hadron Energy",
"country": "USA",
"hqCity": "San Francisco",
"reactorType": "Water-cooled",
"spectrum": "Thermal",
"outletTemp": 300,
"thermal": 35,
"gross": 10,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": false,
"offGrid": true,
"notes": "Hadron Energy is developing the Halo 10, a 10 MWe (35 MWt) PWR with outlet temperature of 300°C. The reactor will use LEU+ (5-20% enriched) uranium fuel and will have a 10 year refuelling cycle. Target applications include data centres, off-grid / remote communities and industrial facilities.\n\nThe company has submitted a Letter of Intent, Regulatory Engagement Plan, and Quality Assurance Program Description to the US NRC, initiating pre-application activities. Hadron Energy is planning to list publicly via a $1.2 billion business combination with GigCapital7 Corp.",
"latitude": 37.527028745812,
"longitude": -122.26293881713,
"newsLink1": "https://www.world-nuclear-news.org/articles/micro-modular-reactor-company-to-go-public ||| Micro modular reactor company Hadron Energy plans to go public ||| October 2025",
"newsLink2": "",
"newsLink3": ""
},
{
"name": "Allseas HTGR",
"developer": "Allseas Engineering B.V.",
"country": "Netherlands",
"hqCity": "Delft",
"reactorType": "Gas-cooled",
"spectrum": "Thermal",
"outletTemp": 700,
"thermal": 70,
"gross": 25,
"fuelEnrichment": "5-20%",
"designStatus": "Design & development",
"electricity": true,
"lowTempHeat": true,
"highTempHeat": true,
"offGrid": true,
"notes": "Dutch offshore construction engineering contractor Allseas launched in June 2025 a five-year plan to design, develop and deploy a small modular reactor tailored for integration into offshore vessels and for onshore use.\n\nThe Allseas HTGR is a 25 MWe (70 MWt) reactor with outlet temperature of 700°C. It will TRISO pebble fuel enriched to between 10 and 20% U-235.",
"latitude": 52.0094699029368,
"longitude": 4.37884566836608,
"newsLink1": "https://www.world-nuclear-news.org/articles/allseas-aims-for-rapid-smr-deployment ||| Allseas aims for rapid SMR deployment ||| June 2025",
"newsLink2": "",
"newsLink3": ""
}
];
// ---- Compare feature state & helpers ----
var smrSelectedCompare = []; // array of reactor names (unique), max 5
function smrUpdateCompareBar() {
var bar = document.getElementById('smrCompareBar');
var list = document.getElementById('smrCompareList');
var btn = document.getElementById('smrCompareBtn');
if (!bar || !list || !btn) return;
if (smrSelectedCompare.length === 0) {
bar.style.display = 'none';
btn.disabled = true;
list.innerHTML = '';
return;
}
bar.style.display = 'flex';
btn.disabled = smrSelectedCompare.length < 2;
var html = '';
for (var i = 0; i < smrSelectedCompare.length; i++) {
var name = smrSelectedCompare[i];
html += '<span class="smr-compare-chip">' + name +
' <button type="button" data-remove="' + name.replace(/'/g, "\\'") + '">&times;</button></span>';
}
list.innerHTML = html;
// bind removal handlers
list.querySelectorAll('button[data-remove]').forEach(function(b){
b.addEventListener('click', function(){
var n = this.getAttribute('data-remove');
smrSelectedCompare = smrSelectedCompare.filter(function(x){ return x !== n; });
// uncheck any checkbox with this name
var cb = document.querySelector('.smr-compare-checkbox[data-name="' + CSS.escape(n) + '"]');
if (cb) cb.checked = false;
smrUpdateCompareBar();
});
});
}
function smrToggleCompare(name, checked) {
if (checked) {
if (smrSelectedCompare.indexOf(name) === -1) {
if (smrSelectedCompare.length >= 5) {
alert('You can compare up to 5 reactors.');
// revert checkbox
var cb = document.querySelector('.smr-compare-checkbox[data-name="' + CSS.escape(name) + '"]');
if (cb) cb.checked = false;
return;
}
smrSelectedCompare.push(name);
}
} else {
smrSelectedCompare = smrSelectedCompare.filter(function(n){ return n !== name; });
}
smrUpdateCompareBar();
}
function smrRenderCompareTable() {
var view = document.getElementById('smrCompareView');
var grid = document.getElementById('smrResultsGrid');
var sidebar = document.getElementById('smrSidebar');
var mainContent = document.getElementById('smrMainContent');
var resultsHeaderEl = document.querySelector('.smr-results-header');
var activeFiltersWrapper = document.getElementById('smrActiveFiltersWrapper');
if (!view) return;
var selected = smrSelectedCompare.map(function(n){ return reactors.find(function(r){ return r.name === n; }); }).filter(Boolean);
if (selected.length < 2) return;
var metrics = [
{key:'developer', label:'Developer'},
{key:'country', label:'Country'},
{key:'reactorType', label:'Reactor Type'},
{key:'spectrum', label:'Spectrum'},
{key:'fuelEnrichment', label:'Fuel Enrichment'},
{key:'outletTemp', label:'Outlet Temp (°C)'},
{key:'thermal', label:'Thermal Capacity (MWt)'},
{key:'gross', label:'Gross Capacity (MWe)'},
{key:'applications', label:'Applications'}
];
function appString(r){
function yesNo(v){ return v ? '✓' : '✗'; }
return 'Elec ' + yesNo(r.electricity) + ' · Low ' + yesNo(r.lowTempHeat) + ' · High ' + yesNo(r.highTempHeat) + ' · Off-grid ' + yesNo(r.offGrid);
}
var table = '<div class="smr-detail-header">' +
'<div class="smr-detail-title">Comparison</div>' +
'<button class="smr-back-btn" id="smrCompareBack">← Return to Results</button>' +
'</div>';
table += '<div class="smr-detail-content">';
table += '<div style="overflow-x:auto;">';
table += '<table class="smr-compare-table" style="width:100%; border-collapse:collapse;">';
// header row
table += '<thead><tr>' +
'<th style="text-align:left; padding:10px; border-bottom:1px solid #e5e7eb;">Metric</th>';
selected.forEach(function(r){
table += '<th style="text-align:left; padding:10px; border-bottom:1px solid #e5e7eb;">' + r.name + '</th>';
});
table += '</tr></thead>';
// body rows
table += '<tbody>';
metrics.forEach(function(m){
table += '<tr>';
table += '<td style="padding:10px; border-bottom:1px solid #f3f4f6; font-weight:600; color:#374151;">' + m.label + '</td>';
selected.forEach(function(r){
var val;
if (m.key === 'applications') {
val = appString(r);
} else {
val = (r[m.key] !== undefined && r[m.key] !== null) ? r[m.key] : '—';
}
table += '<td style="padding:10px; border-bottom:1px solid #f3f4f6; color:#6c757d;">' + val + '</td>';
});
table += '</tr>';
});
table += '</tbody></table></div></div>';
view.innerHTML = table;
// hide the compare bar while in compare view
var cmpBar = document.getElementById('smrCompareBar');
if (cmpBar) cmpBar.style.display = 'none';
// Show compare view; hide grid/side like detail
if (grid) grid.style.display = 'none';
if (sidebar) sidebar.classList.add('hidden');
if (mainContent) mainContent.classList.add('full-width');
if (resultsHeaderEl) resultsHeaderEl.style.display = 'none';
if (activeFiltersWrapper) activeFiltersWrapper.style.display = 'none';
view.classList.add('active');
// bind back
var backBtn = document.getElementById('smrCompareBack');
if (backBtn) {
backBtn.addEventListener('click', function(){
// Clear compare selections
smrSelectedCompare = [];
var allCompareBoxes = document.querySelectorAll('.smr-compare-checkbox');
allCompareBoxes.forEach(function(cb) {
cb.checked = false;
});
smrUpdateCompareBar();
view.classList.remove('active');
view.innerHTML = '';
if (grid) grid.style.display = 'grid';
if (sidebar) sidebar.classList.remove('hidden');
if (mainContent) mainContent.classList.remove('full-width');
if (resultsHeaderEl) resultsHeaderEl.style.display = 'flex';
// show compare bar again if there are selections
var cmpBar2 = document.getElementById('smrCompareBar');
if (cmpBar2) {
cmpBar2.style.display = (smrSelectedCompare.length > 0) ? 'flex' : 'none';
}
// Only show active filters wrapper if there are active filters
var filters = getCurrentFilters();
var hasActiveFilters = filters.rawSearch ||
filters.reactorTypes.length || filters.countries.length || filters.designStatuses.length ||
filters.fuelEnrichments.length || filters.spectrums.length || filters.applications.length ||
filters.outletTempMin > absoluteRanges.outletTemp.min || filters.outletTempMax < absoluteRanges.outletTemp.max ||
filters.thermalMin > absoluteRanges.thermal.min || filters.thermalMax < absoluteRanges.thermal.max ||
filters.grossMin > absoluteRanges.gross.min || filters.grossMax < absoluteRanges.gross.max;
if (activeFiltersWrapper && hasActiveFilters) activeFiltersWrapper.style.display = 'flex';
window.scrollTo({ top: 0, behavior: 'smooth' });
});
}
}
// Hook up the compare button
document.addEventListener('click', function(e){
if (e.target && e.target.id === 'smrCompareBtn') {
smrRenderCompareTable();
}
});
var reactorTypes = [];
var fuelEnrichments = [];
var spectrums = [];
var countries = [];
var designStatuses = [];
var applications = ['Electricity', 'Low-temperature heat', 'High-temperature heat', 'Off-grid']; // NEW
reactors.forEach(function(r) {
if (reactorTypes.indexOf(r.reactorType) === -1) reactorTypes.push(r.reactorType);
if (fuelEnrichments.indexOf(r.fuelEnrichment) === -1) fuelEnrichments.push(r.fuelEnrichment);
if (spectrums.indexOf(r.spectrum) === -1) spectrums.push(r.spectrum);
if (countries.indexOf(r.country) === -1) countries.push(r.country);
if (designStatuses.indexOf(r.designStatus) === -1) designStatuses.push(r.designStatus);
});
reactorTypes.sort();
fuelEnrichments.sort();
spectrums.sort();
countries.sort();
designStatuses.sort();
var outletTemps = reactors.map(function(r) { return r.outletTemp; });
var thermals = reactors.map(function(r) { return r.thermal; });
var grosses = reactors.map(function(r) { return r.gross; });
var absoluteRanges = {
outletTemp: { min: Math.min.apply(null, outletTemps), max: Math.max.apply(null, outletTemps) },
thermal: { min: Math.min.apply(null, thermals), max: Math.max.apply(null, thermals) },
gross: { min: Math.min.apply(null, grosses), max: Math.max.apply(null, grosses) }
};
// -------- Summary charts (Designs summary tab) - Updated for tabbed interface --------
var currentChartType = 'country'; // Default chart type
var chartData = {}; // Store all chart data
function smrBuildBarChart(containerId, counts, title) {
var container = document.getElementById(containerId);
if (!container) return;
var keys = Object.keys(counts || {});
if (!keys.length) {
container.innerHTML = '<div style="font-size:12px;color:#9ca3af;">No data</div>';
return;
}
// Sort by count desc, then label asc
keys.sort(function(a, b) {
var diff = counts[b] - counts[a];
if (diff !== 0) return diff;
return a.localeCompare(b);
});
var max = 0;
for (var i = 0; i < keys.length; i++) {
if (counts[keys[i]] > max) max = counts[keys[i]];
}
if (!max) max = 1;
var html = '';
for (var j = 0; j < keys.length; j++) {
var label = keys[j];
var value = counts[label];
var pct = (value / max) \* 100;
html += '' +
'<div class="smr-chart-bar-row">' +
'<div class="smr-chart-bar-label">' + label + '</div>' +
'<div class="smr-chart-bar-track">' +
'<div class="smr-chart-bar" style="width:' + pct + '%;"></div>' +
'</div>' +
'<div class="smr-chart-bar-value">' + value + '</div>' +
'</div>';
}
container.innerHTML = html;
}
// NEW: Scatter plot function
function prepareChartData() {
chartData.country = {};
chartData.status = {};
chartData.type = {};
chartData.fuel = {};
chartData.power = {};
chartData.temperature = {};
// Find max power for histogram bins
var maxPower = 0;
// Find max temperature for histogram bins
var maxTemp = 0;
for (var i = 0; i < reactors.length; i++) {
var r = reactors[i];
if (r.gross && r.gross > maxPower) {
maxPower = r.gross;
}
if (r.outletTemp && r.outletTemp > maxTemp) {
maxTemp = r.outletTemp;
}
}
// Create power bins (0-50, 50-100, 100-150, etc.)
var powerBinSize = 50;
var numPowerBins = Math.ceil(maxPower / powerBinSize);
for (var b = 0; b < numPowerBins; b++) {
var binLabel = (b \* powerBinSize) + '-' + ((b + 1) \* powerBinSize) + ' MWe';
chartData.power[binLabel] = 0;
}
// Create temperature bins (0-200, 200-400, 400-600, etc.)
var tempBinSize = 200;
var numTempBins = Math.ceil(maxTemp / tempBinSize);
for (var t = 0; t < numTempBins; t++) {
var tempBinLabel = (t \* tempBinSize) + '-' + ((t + 1) \* tempBinSize) + '°C';
chartData.temperature[tempBinLabel] = 0;
}
for (var i = 0; i < reactors.length; i++) {
var r = reactors[i];
if (r.country) {
chartData.country[r.country] = (chartData.country[r.country] || 0) + 1;
}
if (r.designStatus) {
chartData.status[r.designStatus] = (chartData.status[r.designStatus] || 0) + 1;
}
if (r.reactorType) {
chartData.type[r.reactorType] = (chartData.type[r.reactorType] || 0) + 1;
}
if (r.fuelEnrichment) {
chartData.fuel[r.fuelEnrichment] = (chartData.fuel[r.fuelEnrichment] || 0) + 1;
}
// Add to power histogram bins
if (r.gross) {
var powerBinIndex = Math.floor(r.gross / powerBinSize);
var powerBinLabel = (powerBinIndex \* powerBinSize) + '-' + ((powerBinIndex + 1) \* powerBinSize) + ' MWe';
if (chartData.power[powerBinLabel] !== undefined) {
chartData.power[powerBinLabel]++;
}
}
// Add to temperature histogram bins
if (r.outletTemp) {
var tempBinIndex = Math.floor(r.outletTemp / tempBinSize);
var tempBinLabel = (tempBinIndex \* tempBinSize) + '-' + ((tempBinIndex + 1) \* tempBinSize) + '°C';
if (chartData.temperature[tempBinLabel] !== undefined) {
chartData.temperature[tempBinLabel]++;
}
}
}
}
function smrBuildHistogram(containerId, counts, title) {
var container = document.getElementById(containerId);
if (!container) return;
var keys = Object.keys(counts || {});
if (!keys.length) {
container.innerHTML = '<div style="font-size:12px;color:#9ca3af;">No data</div>';
return;
}
// Sort bins by power range (extract starting number and sort numerically)
keys.sort(function(a, b) {
var aStart = parseInt(a.split('-')[0]);
var bStart = parseInt(b.split('-')[0]);
return aStart - bStart;
});
var max = 0;
for (var i = 0; i < keys.length; i++) {
if (counts[keys[i]] > max) max = counts[keys[i]];
}
if (!max) max = 1;
var html = '<div class="smr-histogram-chart">';
for (var j = 0; j < keys.length; j++) {
var label = keys[j];
var value = counts[label];
var heightPct = (value / max) \* 100;
html += '' +
'<div class="smr-histogram-bar-container">' +
'<div class="smr-histogram-value">' + value + '</div>' +
'<div class="smr-histogram-bar" style="height:' + heightPct + '%;"></div>' +
'<div class="smr-histogram-label">' + label + '</div>' +
'</div>';
}
html += '</div>';
container.innerHTML = html;
}
var currentHistogramType = 'power'; // Default histogram type
function showHistogram(histogramType) {
currentHistogramType = histogramType;
if (histogramType === 'power') {
smrBuildHistogram('smrHistogramChart', chartData.power, 'Power Output Distribution');
} else if (histogramType === 'temperature') {
smrBuildHistogram('smrHistogramChart', chartData.temperature, 'Outlet Temperature Distribution');
}
// Update active tab
var histogramTabs = document.querySelectorAll('.smr-histogram-tab');
histogramTabs.forEach(function(tab) {
tab.classList.remove('active');
if (tab.getAttribute('data-histogram') === histogramType) {
tab.classList.add('active');
}
});
}
function showChart(chartType) {
var titles = {
country: 'Designs by country',
type: 'Designs by reactor type',
status: 'Designs by design status',
fuel: 'Designs by fuel enrichment'
};
currentChartType = chartType;
smrBuildBarChart('smrChart', chartData[chartType], titles[chartType]);
// Update active tab
var tabs = document.querySelectorAll('.smr-chart-tab');
tabs.forEach(function(tab) {
tab.classList.remove('active');
if (tab.getAttribute('data-chart') === chartType) {
tab.classList.add('active');
}
});
}
function renderSummaryCharts() {
var totalDesigns = reactors.length;
// Calculate unique developers
var uniqueDevelopers = new Set();
reactors.forEach(function(reactor) {
if (reactor.developer) {
uniqueDevelopers.add(reactor.developer.trim());
}
});
var totalDevelopers = uniqueDevelopers.size;
// Calculate unique countries
var uniqueCountries = new Set();
reactors.forEach(function(reactor) {
if (reactor.country) {
uniqueCountries.add(reactor.country.trim());
}
});
var totalCountries = uniqueCountries.size;
// Update summary statistics
var designsNumberEl = document.getElementById('smrStatDesignsNumber');
if (designsNumberEl) {
designsNumberEl.textContent = totalDesigns;
}
var developersNumberEl = document.getElementById('smrStatDevelopersNumber');
if (developersNumberEl) {
developersNumberEl.textContent = totalDevelopers;
}
var countriesNumberEl = document.getElementById('smrStatCountriesNumber');
if (countriesNumberEl) {
countriesNumberEl.textContent = totalCountries;
}
prepareChartData();
showChart(currentChartType); // Show current chart type
// Render default histogram (power)
showHistogram(currentHistogramType);
// Add chart tab event listeners
var chartTabs = document.querySelectorAll('.smr-chart-tab');
chartTabs.forEach(function(tab) {
tab.addEventListener('click', function() {
var chartType = this.getAttribute('data-chart');
showChart(chartType);
});
});
// Add histogram tab event listeners
var histogramTabs = document.querySelectorAll('.smr-histogram-tab');
histogramTabs.forEach(function(tab) {
tab.addEventListener('click', function() {
var histogramType = this.getAttribute('data-histogram');
showHistogram(histogramType);
});
});
}
function initializeFilters() {
var reactorTypeDiv = document.getElementById('smrReactorTypeFilter');
reactorTypes.forEach(function(type) {
var count = reactors.filter(function(r) { return r.reactorType === type; }).length;
var label = document.createElement('label');
var checkbox = document.createElement('input');
checkbox.type = 'checkbox';
checkbox.value = type;
checkbox.checked = false;
checkbox.addEventListener('change', applyFilters);
label.appendChild(checkbox);
label.appendChild(document.createTextNode(' ' + type + ' (' + count + ')'));
reactorTypeDiv.appendChild(label);
});
var countryDiv = document.getElementById('smrCountryFilter');
if (countryDiv) {
countries.forEach(function(country) {
var count = reactors.filter(function(r) { return r.country === country; }).length;
var label = document.createElement('label');
var checkbox = document.createElement('input');
checkbox.type = 'checkbox';
checkbox.value = country;
checkbox.checked = false;
checkbox.addEventListener('change', applyFilters);
label.appendChild(checkbox);
label.appendChild(document.createTextNode(' ' + country + ' (' + count + ')'));
countryDiv.appendChild(label);
});
}
var designStatusDiv = document.getElementById('smrDesignStatusFilter');
if (designStatusDiv) {
designStatuses.forEach(function(status) {
var count = reactors.filter(function(r) { return r.designStatus === status; }).length;
var label = document.createElement('label');
var checkbox = document.createElement('input');
checkbox.type = 'checkbox';
checkbox.value = status;
checkbox.checked = false;
checkbox.addEventListener('change', applyFilters);
label.appendChild(checkbox);
label.appendChild(document.createTextNode(' ' + status + ' (' + count + ')'));
designStatusDiv.appendChild(label);
});
}
var fuelDiv = document.getElementById('smrFuelEnrichmentFilter');
fuelEnrichments.forEach(function(fuel) {
var count = reactors.filter(function(r) { return r.fuelEnrichment === fuel; }).length;
var label = document.createElement('label');
var checkbox = document.createElement('input');
checkbox.type = 'checkbox';
checkbox.value = fuel;
checkbox.checked = false;
checkbox.addEventListener('change', applyFilters);
label.appendChild(checkbox);
label.appendChild(document.createTextNode(' ' + fuel + ' (' + count + ')'));
fuelDiv.appendChild(label);
});
var spectrumDiv = document.getElementById('smrSpectrumFilter');
spectrums.forEach(function(spec) {
var count = reactors.filter(function(r) { return r.spectrum === spec; }).length;
var label = document.createElement('label');
var checkbox = document.createElement('input');
checkbox.type = 'checkbox';
checkbox.value = spec;
checkbox.checked = false;
checkbox.addEventListener('change', applyFilters);
label.appendChild(checkbox);
label.appendChild(document.createTextNode(' ' + spec + ' (' + count + ')'));
spectrumDiv.appendChild(label);
});
// NEW: Applications filter initialization
var applicationsDiv = document.getElementById('smrApplicationsFilter');
if (applicationsDiv) {
applications.forEach(function(app) {
var appKey = app === 'Electricity' ? 'electricity' :
app === 'Low-temperature heat' ? 'lowTempHeat' :
app === 'High-temperature heat' ? 'highTempHeat' : 'offGrid';
var count = reactors.filter(function(r) { return r[appKey]; }).length;
var label = document.createElement('label');
var checkbox = document.createElement('input');
checkbox.type = 'checkbox';
checkbox.value = app;
checkbox.checked = false;
checkbox.addEventListener('change', applyFilters);
label.appendChild(checkbox);
label.appendChild(document.createTextNode(' ' + app + ' (' + count + ')'));
applicationsDiv.appendChild(label);
});
}
document.getElementById('smrOutletTempMin').value = absoluteRanges.outletTemp.min;
document.getElementById('smrOutletTempMax').value = absoluteRanges.outletTemp.max;
document.getElementById('smrThermalMin').value = absoluteRanges.thermal.min;
document.getElementById('smrThermalMax').value = absoluteRanges.thermal.max;
document.getElementById('smrGrossMin').value = absoluteRanges.gross.min;
document.getElementById('smrGrossMax').value = absoluteRanges.gross.max;
var reactorTypeToggle = document.getElementById('reactorTypeToggle');
if (reactorTypeToggle) {
reactorTypeToggle.addEventListener('click', function() {
var content = document.getElementById('smrReactorTypeFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'flex';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var countryToggle = document.getElementById('countryToggle');
if (countryToggle) {
countryToggle.addEventListener('click', function() {
var content = document.getElementById('smrCountryFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'flex';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var designStatusToggle = document.getElementById('smrDesignStatusToggle');
if (designStatusToggle) {
designStatusToggle.addEventListener('click', function() {
var content = document.getElementById('smrDesignStatusFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'flex';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var fuelEnrichmentToggle = document.getElementById('fuelEnrichmentToggle');
if (fuelEnrichmentToggle) {
fuelEnrichmentToggle.addEventListener('click', function() {
var content = document.getElementById('smrFuelEnrichmentFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'flex';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var spectrumToggle = document.getElementById('spectrumToggle');
if (spectrumToggle) {
spectrumToggle.addEventListener('click', function() {
var content = document.getElementById('smrSpectrumFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'flex';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
// NEW: Applications toggle
var applicationsToggle = document.getElementById('applicationsToggle');
if (applicationsToggle) {
applicationsToggle.addEventListener('click', function() {
var content = document.getElementById('smrApplicationsFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'flex';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var outletTempToggle = document.getElementById('outletTempToggle');
if (outletTempToggle) {
outletTempToggle.addEventListener('click', function() {
var content = document.getElementById('smrOutletTempFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'block';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var thermalToggle = document.getElementById('thermalToggle');
if (thermalToggle) {
thermalToggle.addEventListener('click', function() {
var content = document.getElementById('smrThermalFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'block';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
var grossToggle = document.getElementById('grossToggle');
if (grossToggle) {
grossToggle.addEventListener('click', function() {
var content = document.getElementById('smrGrossFilter');
var arrow = this.querySelector('.smr-arrow');
if (content.style.display === 'none' || content.style.display === '') {
content.style.display = 'block';
arrow.classList.add('expanded');
} else {
content.style.display = 'none';
arrow.classList.remove('expanded');
}
});
}
}
function getCurrentFilters() {
var checkboxes = document.querySelectorAll('#smrReactorTypeFilter input:checked');
var selectedReactorTypes = [];
for (var i = 0; i < checkboxes.length; i++) {
selectedReactorTypes.push(checkboxes[i].value);
}
checkboxes = document.querySelectorAll('#smrCountryFilter input:checked');
var selectedCountries = [];
for (var i = 0; i < checkboxes.length; i++) {
selectedCountries.push(checkboxes[i].value);
}
checkboxes = document.querySelectorAll('#smrDesignStatusFilter input:checked');
var selectedDesignStatuses = [];
for (var i = 0; i < checkboxes.length; i++) {
selectedDesignStatuses.push(checkboxes[i].value);
}
checkboxes = document.querySelectorAll('#smrFuelEnrichmentFilter input:checked');
var selectedFuel = [];
for (var k = 0; k < checkboxes.length; k++) {
selectedFuel.push(checkboxes[k].value);
}
checkboxes = document.querySelectorAll('#smrSpectrumFilter input:checked');
var selectedSpectrum = [];
for (var m = 0; m < checkboxes.length; m++) {
selectedSpectrum.push(checkboxes[m].value);
}
// NEW: Get selected applications
checkboxes = document.querySelectorAll('#smrApplicationsFilter input:checked');
var selectedApplications = [];
for (var n = 0; n < checkboxes.length; n++) {
selectedApplications.push(checkboxes[n].value);
}
var searchValue = '';
var desktopSearch = document.getElementById('smrSearchInput');
var mobileSearch = document.getElementById('smrSearchInputMobile');
if (desktopSearch && desktopSearch.value) {
searchValue = desktopSearch.value;
} else if (mobileSearch && mobileSearch.value) {
searchValue = mobileSearch.value;
}
return {
search: (searchValue || '').toLowerCase().trim(),
rawSearch: searchValue || '',
reactorTypes: selectedReactorTypes,
countries: selectedCountries,
designStatuses: selectedDesignStatuses,
fuelEnrichments: selectedFuel,
spectrums: selectedSpectrum,
applications: selectedApplications, // NEW
outletTempMin: Number(document.getElementById('smrOutletTempMin').value),
outletTempMax: Number(document.getElementById('smrOutletTempMax').value),
thermalMin: Number(document.getElementById('smrThermalMin').value),
thermalMax: Number(document.getElementById('smrThermalMax').value),
grossMin: Number(document.getElementById('smrGrossMin').value),
grossMax: Number(document.getElementById('smrGrossMax').value)
};
}
function getFilteredReactors() {
var filters = getCurrentFilters();
var filtered = [];
for (var i = 0; i < reactors.length; i++) {
var reactor = reactors[i];
if (filters.search) {
var searchable = (
reactor.name + ' ' +
reactor.developer + ' ' +
reactor.country + ' ' +
reactor.reactorType + ' ' +
reactor.spectrum + ' ' +
reactor.fuelEnrichment + ' ' +
reactor.designStatus
).toLowerCase();
if (searchable.indexOf(filters.search) === -1) continue;
}
if (filters.reactorTypes.length && filters.reactorTypes.indexOf(reactor.reactorType) === -1) continue;
if (filters.countries.length && filters.countries.indexOf(reactor.country) === -1) continue;
if (filters.designStatuses.length && filters.designStatuses.indexOf(reactor.designStatus) === -1) continue;
if (filters.fuelEnrichments.length && filters.fuelEnrichments.indexOf(reactor.fuelEnrichment) === -1) continue;
if (filters.spectrums.length && filters.spectrums.indexOf(reactor.spectrum) === -1) continue;
// NEW: Application filter logic - reactor matches if it has ANY of the selected applications
if (filters.applications.length) {
var matchesAnyApplication = false;
for (var j = 0; j < filters.applications.length; j++) {
var app = filters.applications[j];
if (app === 'Electricity' && reactor.electricity) {
matchesAnyApplication = true;
break;
} else if (app === 'Low-temperature heat' && reactor.lowTempHeat) {
matchesAnyApplication = true;
break;
} else if (app === 'High-temperature heat' && reactor.highTempHeat) {
matchesAnyApplication = true;
break;
} else if (app === 'Off-grid' && reactor.offGrid) {
matchesAnyApplication = true;
break;
}
}
if (!matchesAnyApplication) continue;
}
if (reactor.outletTemp < filters.outletTempMin || reactor.outletTemp > filters.outletTempMax) continue;
if (reactor.thermal < filters.thermalMin || reactor.thermal > filters.thermalMax) continue;
if (reactor.gross < filters.grossMin || reactor.gross > filters.grossMax) continue;
filtered.push(reactor);
}
return filtered;
}
function updateFilterOptions() {
var filtered = getFilteredReactors();
if (filtered.length > 0) {
var outletTemps = filtered.map(function(r) { return r.outletTemp; });
var thermals = filtered.map(function(r) { return r.thermal; });
var grosses = filtered.map(function(r) { return r.gross; });
var availableRanges = {
outletTemp: { min: Math.min.apply(null, outletTemps), max: Math.max.apply(null, outletTemps) },
thermal: { min: Math.min.apply(null, thermals), max: Math.max.apply(null, thermals) },
gross: { min: Math.min.apply(null, grosses), max: Math.max.apply(null, grosses) }
};
var outletMinInput = document.getElementById('smrOutletTempMin');
var outletMaxInput = document.getElementById('smrOutletTempMax');
var currentOutletMin = Number(outletMinInput.value);
var currentOutletMax = Number(outletMaxInput.value);
if (availableRanges.outletTemp.min < currentOutletMin) {
outletMinInput.value = availableRanges.outletTemp.min;
}
if (availableRanges.outletTemp.max > currentOutletMax) {
outletMaxInput.value = availableRanges.outletTemp.max;
}
var thermalMinInput = document.getElementById('smrThermalMin');
var thermalMaxInput = document.getElementById('smrThermalMax');
var currentThermalMin = Number(thermalMinInput.value);
var currentThermalMax = Number(thermalMaxInput.value);
if (availableRanges.thermal.min < currentThermalMin) {
thermalMinInput.value = availableRanges.thermal.min;
}
if (availableRanges.thermal.max > currentThermalMax) {
thermalMaxInput.value = availableRanges.thermal.max;
}
var grossMinInput = document.getElementById('smrGrossMin');
var grossMaxInput = document.getElementById('smrGrossMax');
var currentGrossMin = Number(grossMinInput.value);
var currentGrossMax = Number(grossMaxInput.value);
if (availableRanges.gross.min < currentGrossMin) {
grossMinInput.value = availableRanges.gross.min;
}
if (availableRanges.gross.max > currentGrossMax) {
grossMaxInput.value = availableRanges.gross.max;
}
}
}
// Remove individual filter chip
window.smrRemoveFilter = function(filterType, filterValue) {
if (filterType === 'search') {
var desktopSearch = document.getElementById('smrSearchInput');
var mobileSearch = document.getElementById('smrSearchInputMobile');
if (desktopSearch) desktopSearch.value = '';
if (mobileSearch) mobileSearch.value = '';
} else if (filterType === 'reactorType') {
var checkbox = document.querySelector('#smrReactorTypeFilter input[value="' + filterValue + '"]');
if (checkbox) checkbox.checked = false;
} else if (filterType === 'country') {
var checkbox = document.querySelector('#smrCountryFilter input[value="' + filterValue + '"]');
if (checkbox) checkbox.checked = false;
} else if (filterType === 'designStatus') {
var checkbox = document.querySelector('#smrDesignStatusFilter input[value="' + filterValue + '"]');
if (checkbox) checkbox.checked = false;
} else if (filterType === 'fuelEnrichment') {
var checkbox = document.querySelector('#smrFuelEnrichmentFilter input[value="' + filterValue + '"]');
if (checkbox) checkbox.checked = false;
} else if (filterType === 'spectrum') {
var checkbox = document.querySelector('#smrSpectrumFilter input[value="' + filterValue + '"]');
if (checkbox) checkbox.checked = false;
} else if (filterType === 'application') { // NEW
var checkbox = document.querySelector('#smrApplicationsFilter input[value="' + filterValue + '"]');
if (checkbox) checkbox.checked = false;
} else if (filterType === 'outletTemp') {
document.getElementById('smrOutletTempMin').value = absoluteRanges.outletTemp.min;
document.getElementById('smrOutletTempMax').value = absoluteRanges.outletTemp.max;
} else if (filterType === 'thermal') {
document.getElementById('smrThermalMin').value = absoluteRanges.thermal.min;
document.getElementById('smrThermalMax').value = absoluteRanges.thermal.max;
} else if (filterType === 'gross') {
document.getElementById('smrGrossMin').value = absoluteRanges.gross.min;
document.getElementById('smrGrossMax').value = absoluteRanges.gross.max;
}
applyFilters();
};
function updateActiveFiltersSummary() {
var container = document.getElementById('smrFilterChips');
if (!container) return;
var filters = getCurrentFilters();
var chips = [];
// Search chip
if (filters.rawSearch && filters.rawSearch.trim() !== '') {
chips.push({
type: 'search',
label: 'Search: "' + filters.rawSearch.trim() + '"',
value: filters.rawSearch.trim()
});
}
// Reactor Type chips
if (filters.reactorTypes.length && filters.reactorTypes.length < reactorTypes.length) {
filters.reactorTypes.forEach(function(type) {
chips.push({
type: 'reactorType',
label: type,
value: type
});
});
}
// Country chips
if (filters.countries.length && filters.countries.length < countries.length) {
filters.countries.forEach(function(country) {
chips.push({
type: 'country',
label: country,
value: country
});
});
}
// Design Status chips
if (filters.designStatuses.length && filters.designStatuses.length < designStatuses.length) {
filters.designStatuses.forEach(function(status) {
chips.push({
type: 'designStatus',
label: status,
value: status
});
});
}
// Spectrum chips
if (filters.spectrums.length && filters.spectrums.length < spectrums.length) {
filters.spectrums.forEach(function(spectrum) {
chips.push({
type: 'spectrum',
label: spectrum,
value: spectrum
});
});
}
// Fuel Enrichment chips
if (filters.fuelEnrichments.length && filters.fuelEnrichments.length < fuelEnrichments.length) {
filters.fuelEnrichments.forEach(function(fuel) {
chips.push({
type: 'fuelEnrichment',
label: fuel,
value: fuel
});
});
}
// NEW: Application chips
if (filters.applications.length && filters.applications.length < applications.length) {
filters.applications.forEach(function(app) {
chips.push({
type: 'application',
label: app,
value: app
});
});
}
// Outlet Temp range chip
if (filters.outletTempMin > absoluteRanges.outletTemp.min || filters.outletTempMax < absoluteRanges.outletTemp.max) {
chips.push({
type: 'outletTemp',
label: 'Outlet: ' + filters.outletTempMin + '–' + filters.outletTempMax + '°C',
value: null
});
}
// Thermal range chip
if (filters.thermalMin > absoluteRanges.thermal.min || filters.thermalMax < absoluteRanges.thermal.max) {
chips.push({
type: 'thermal',
label: 'Thermal: ' + filters.thermalMin + '–' + filters.thermalMax + ' MWt',
value: null
});
}
// Gross range chip
if (filters.grossMin > absoluteRanges.gross.min || filters.grossMax < absoluteRanges.gross.max) {
chips.push({
type: 'gross',
label: 'Gross: ' + filters.grossMin + '–' + filters.grossMax + ' MWe',
value: null
});
}
// Render chips
var html = '';
chips.forEach(function(chip) {
var value = chip.value !== null ? chip.value.replace(/'/g, "\\'") : '';
html += '<div class="smr-filter-chip">' +
'<span>' + chip.label + '</span>' +
'<button class="smr-chip-remove" onclick="window.smrRemoveFilter(\'' + chip.type + '\', \'' + value + '\')" aria-label="Remove filter">&times;</button>' +
'</div>';
});
container.innerHTML = html;
// Show/hide the "Clear all filters" button
var clearBtn = document.getElementById('smrClearFiltersBtn');
var wrapper = document.getElementById('smrActiveFiltersWrapper');
if (chips.length === 0) {
if (wrapper) wrapper.style.display = 'none';
} else {
if (wrapper) wrapper.style.display = 'flex';
}
}
function renderResults() {
var filtered = getFilteredReactors();
var grid = document.getElementById('smrResultsGrid');
var countDiv = document.getElementById('smrResultsCount');
var detailView = document.getElementById('smrDetailView');
var resultsHeaderEl = document.querySelector('.smr-results-header');
var activeFiltersWrapper = document.getElementById('smrActiveFiltersWrapper');
if (detailView) {
detailView.classList.remove('active');
detailView.innerHTML = '';
}
if (grid) grid.style.display = 'grid';
if (sidebar) sidebar.classList.remove('hidden');
if (mainContent) mainContent.classList.remove('full-width');
if (resultsHeaderEl) resultsHeaderEl.style.display = 'flex';
// show compare bar again if there are selections
var cmpBar2 = document.getElementById('smrCompareBar');
if (cmpBar2) {
cmpBar2.style.display = (smrSelectedCompare.length > 0) ? 'flex' : 'none';
}
var sortSelect = document.getElementById('smrSortSelect');
var sortBy = sortSelect ? sortSelect.value : 'name';
filtered.sort(function(a, b) {
if (sortBy === 'name') {
return a.name.localeCompare(b.name);
} else if (sortBy === 'country') {
return a.country.localeCompare(b.country);
} else if (sortBy === 'outletTemp') {
return b.outletTemp - a.outletTemp;
} else if (sortBy === 'thermal') {
return b.thermal - a.thermal;
} else if (sortBy === 'gross') {
return b.gross - a.gross;
}
return 0;
});
countDiv.textContent = 'Showing ' + filtered.length + ' of ' + reactors.length + ' reactors';
if (filtered.length === 0) {
grid.innerHTML = '<div class="smr-no-results">No reactors match your filters</div>';
return;
}
var html = '';
for (var i = 0; i < filtered.length; i++) {
var reactor = filtered[i];
html += '<div class="smr-reactor-card">' +'<label class="smr-compare-select">' +'<input type="checkbox" class="smr-compare-checkbox" data-name="' + reactor.name.replace(/'/g, "\\'") + '"> Select to compare' +'</label>' +'<div class="smr-reactor-name">' + reactor.name + '</div>' +
'<div class="smr-reactor-meta">' +
'<span class="smr-badge">' + reactor.country + '</span>' +
'<span class="smr-badge">' + reactor.spectrum + '</span>' +
'<span class="smr-badge">' + reactor.reactorType + '</span>' +
'</div>' +
'<div class="smr-reactor-details">' +
'<div><strong>Developer:</strong> ' + reactor.developer + '</div>' +
'<div><strong>Design Status:</strong> ' + reactor.designStatus + '</div>' +
'<div><strong>Fuel Enrichment:</strong> ' + reactor.fuelEnrichment + '</div>' +
'<div><strong>Outlet Temp:</strong> ' + reactor.outletTemp + '°C</div>' +
'<div><strong>Thermal Capacity:</strong> ' + reactor.thermal + ' MWt</div>' +
'<div><strong>Gross Capacity:</strong> ' + reactor.gross + ' MWe</div>' +
'</div>' +
'<button class="smr-detail-btn" onclick="window.showReactorDetail(\'' + reactor.name.replace(/'/g, "\\'") + '\')">Detailed Information</button>' +
'</div>';
}
grid.innerHTML = html;
// bind compare checkbox listeners
var boxes = grid.querySelectorAll('.smr-compare-checkbox');
boxes.forEach(function(cb){
var name = cb.getAttribute('data-name');
cb.checked = smrSelectedCompare.indexOf(name) !== -1;
cb.addEventListener('change', function(){
smrToggleCompare(name, cb.checked);
});
});
smrUpdateCompareBar();
}
function showReactorDetail(name, skipURLUpdate) {
var reactor = reactors.find(function(r) { return r.name === name; });
if (!reactor) return;
scrollPosition = window.pageYOffset || document.documentElement.scrollTop;
var detailView = document.getElementById('smrDetailView');
var grid = document.getElementById('smrResultsGrid');
var sidebar = document.getElementById('smrSidebar');
var mainContent = document.getElementById('smrMainContent');
var resultsHeaderEl = document.querySelector('.smr-results-header');
var activeFiltersWrapper = document.getElementById('smrActiveFiltersWrapper');
// Build applications inline string
var applicationsHTML = '';
applicationsHTML += '<span class="smr-application-inline">' +
'<span class="smr-application-inline-icon ' + (reactor.electricity ? 'yes' : 'no') + '">' +
(reactor.electricity ? '✓' : '✗') + '</span> Electricity</span>';
applicationsHTML += '<span class="smr-application-inline">' +
'<span class="smr-application-inline-icon ' + (reactor.lowTempHeat ? 'yes' : 'no') + '">' +
(reactor.lowTempHeat ? '✓' : '✗') + '</span> Low-temp heat</span>';
applicationsHTML += '<span class="smr-application-inline">' +
'<span class="smr-application-inline-icon ' + (reactor.highTempHeat ? 'yes' : 'no') + '">' +
(reactor.highTempHeat ? '✓' : '✗') + '</span> High-temp heat</span>';
applicationsHTML += '<span class="smr-application-inline">' +
'<span class="smr-application-inline-icon ' + (reactor.offGrid ? 'yes' : 'no') + '">' +
(reactor.offGrid ? '✓' : '✗') + '</span> Off-grid</span>';
detailView.innerHTML =
'<div class="smr-detail-header">' +
'<div class="smr-detail-title">' + reactor.name + '</div>' +
'<button class="smr-back-btn" onclick="window.hideReactorDetail()">← Return to Results</button>' +
'</div>' +
'<div class="smr-detail-content">' +
'<div class="smr-detail-meta">' +
'<span class="smr-badge">' + reactor.country + '</span>' +
'<span class="smr-badge">' + reactor.spectrum + '</span>' +
'<span class="smr-badge">' + reactor.reactorType + '</span>' +
'</div>' +
'<div class="smr-detail-specs">' +
'<div><strong>Developer:</strong> ' + reactor.developer + '</div>' +
'<div><strong>Design Status:</strong> ' + reactor.designStatus + '</div>' +
'<div><strong>Fuel Enrichment:</strong> ' + reactor.fuelEnrichment + '</div>' +
'<div><strong>Outlet Temperature:</strong> ' + reactor.outletTemp + ' °C</div>' +
'<div><strong>Thermal Capacity:</strong> ' + reactor.thermal + ' MWt</div>' +
'<div><strong>Gross Capacity:</strong> ' + reactor.gross + ' MWe</div>' +
'<div><strong>Applications:</strong> ' + applicationsHTML + '</div>' +
'</div>' +
'<div>' +
'<div class="smr-detail-notes-heading">Latest News</div>' +
'<div class="smr-notes-content">' +
(function() {
var newsItems = [];
// Function to format date as "Month Year"
function formatDate(dateStr) {
try {
var date = new Date(dateStr);
if (isNaN(date.getTime())) {
// If date parsing fails, return the original string
return dateStr;
}
var months = ['January', 'February', 'March', 'April', 'May', 'June',
'July', 'August', 'September', 'October', 'November', 'December'];
return months[date.getMonth()] + ' ' + date.getFullYear();
} catch (e) {
return dateStr;
}
}
// Process each news link field
[reactor.newsLink1, reactor.newsLink2, reactor.newsLink3].forEach(function(linkData) {
if (linkData && linkData.trim() !== '') {
var parts = linkData.split('|||');
if (parts.length >= 3) {
// Format: URL|||Headline|||Date
var url = parts[0].trim();
var headline = parts[1].trim();
var dateStr = parts[2].trim();
var formattedDate = formatDate(dateStr);
newsItems.push('<a href="' + url + '" target="\_blank" rel="noopener noreferrer">' + formattedDate + ' – ' + headline + '</a>');
} else if (parts.length === 1) {
// Fallback: just URL, use generic text
var url = parts[0].trim();
newsItems.push('<a href="' + url + '" target="\_blank" rel="noopener noreferrer">News Article</a>');
}
}
});
if (newsItems.length === 0) {
return 'N/A';
} else {
return newsItems.join('<br><br>');
}
})() +
'</div>' +
'</div>' +
'<div>' +
'<div class="smr-detail-notes-heading">Additional Information</div>' +
'<div class="smr-notes-content">' + (reactor.notes || 'No additional information available.') + '</div>' +
'</div>' +
'</div>';
grid.style.display = 'none';
sidebar.classList.add('hidden');
mainContent.classList.add('full-width');
if (resultsHeaderEl) resultsHeaderEl.style.display = 'none';
if (activeFiltersWrapper) activeFiltersWrapper.style.display = 'none';
detailView.classList.add('active');
// Update URL with detail parameter
if (!skipURLUpdate) {
updateURL(false);
}
setTimeout(function() {
if (window.innerWidth > 768) {
window.scrollTo({
top: 0,
behavior: 'smooth'
});
} else {
var tabsWrapper = document.querySelector('.smr-tabs-wrapper');
var tabsHeight = tabsWrapper ? tabsWrapper.offsetHeight : 0;
var detailTop = detailView.getBoundingClientRect().top + window.pageYOffset;
window.scrollTo({
top: detailTop - tabsHeight,
behavior: 'smooth'
});
}
}, 50);
}
function hideReactorDetail() {
// Use browser back navigation for better UX
history.back();
}
function hideReactorDetailDirect() {
// Clear compare selections
smrSelectedCompare = [];
var allCompareBoxes = document.querySelectorAll('.smr-compare-checkbox');
allCompareBoxes.forEach(function(cb) {
cb.checked = false;
});
smrUpdateCompareBar();
var detailView = document.getElementById('smrDetailView');
var grid = document.getElementById('smrResultsGrid');
var sidebar = document.getElementById('smrSidebar');
var mainContent = document.getElementById('smrMainContent');
var resultsHeaderEl = document.querySelector('.smr-results-header');
var activeFiltersWrapper = document.getElementById('smrActiveFiltersWrapper');
detailView.classList.remove('active');
detailView.innerHTML = '';
grid.style.display = 'grid';
sidebar.classList.remove('hidden');
mainContent.classList.remove('full-width');
if (resultsHeaderEl) resultsHeaderEl.style.display = 'flex';
// show compare bar again if there are selections
var cmpBar2 = document.getElementById('smrCompareBar');
if (cmpBar2) {
cmpBar2.style.display = (smrSelectedCompare.length > 0) ? 'flex' : 'none';
}
// Only show active filters wrapper if there are active filters
var filters = getCurrentFilters();
var hasActiveFilters = filters.rawSearch ||
filters.reactorTypes.length ||
filters.countries.length ||
filters.designStatuses.length ||
filters.fuelEnrichments.length ||
filters.spectrums.length ||
filters.applications.length || // NEW
filters.outletTempMin > absoluteRanges.outletTemp.min ||
filters.outletTempMax < absoluteRanges.outletTemp.max ||
filters.thermalMin > absoluteRanges.thermal.min ||
filters.thermalMax < absoluteRanges.thermal.max ||
filters.grossMin > absoluteRanges.gross.min ||
filters.grossMax < absoluteRanges.gross.max;
if (activeFiltersWrapper && hasActiveFilters) {
activeFiltersWrapper.style.display = 'flex';
}
setTimeout(function() {
window.scrollTo({
top: scrollPosition,
behavior: 'smooth'
});
}, 50);
}
window.showReactorDetail = showReactorDetail;
window.hideReactorDetail = hideReactorDetail;
// NEW: skeleton loader for results grid
function showLoadingSkeleton() {
var grid = document.getElementById('smrResultsGrid');
if (!grid) return;
var skeletonCount = Math.min(6, reactors.length);
var html = '';
for (var i = 0; i < skeletonCount; i++) {
html += '<div class="smr-reactor-card smr-skeleton-card">' +
'<div class="smr-skeleton-title"></div>' +
'<div class="smr-reactor-meta">' +
'<span class="smr-skeleton-badge"></span>' +
'<span class="smr-skeleton-badge"></span>' +
'<span class="smr-skeleton-badge"></span>' +
'</div>' +
'<div class="smr-reactor-details">' +
'<div class="smr-skeleton-line"></div>' +
'<div class="smr-skeleton-line"></div>' +
'<div class="smr-skeleton-line"></div>' +
'<div class="smr-skeleton-line short"></div>' +
'</div>' +
'<div class="smr-skeleton-button"></div>' +
'</div>';
}
grid.innerHTML = html;
// bind compare checkbox listeners
var boxes = grid.querySelectorAll('.smr-compare-checkbox');
boxes.forEach(function(cb){
var name = cb.getAttribute('data-name');
cb.checked = smrSelectedCompare.indexOf(name) !== -1;
cb.addEventListener('change', function(){
smrToggleCompare(name, cb.checked);
});
});
smrUpdateCompareBar();
}
function applyFilters(skipURLUpdate) {
var grid = document.getElementById('smrResultsGrid');
// Add loading state and show skeleton cards
if (grid) {
grid.classList.add('loading');
showLoadingSkeleton();
}
// Use timeout to allow skeletons to render before processing
setTimeout(function() {
renderResults();
updateFilterOptions();
updateActiveFiltersSummary();
// Update URL unless explicitly skipped (e.g., during initial load or popstate)
if (!skipURLUpdate) {
updateURL(false);
}
if (grid) {
grid.classList.remove('loading');
}
}, 150);
}
var desktopSearchInput = document.getElementById('smrSearchInput');
var mobileSearchInput = document.getElementById('smrSearchInputMobile');
var searchDebounceTimer = null;
function handleSearchInput(event) {
var value = event.target.value;
if (desktopSearchInput && event.target !== desktopSearchInput) {
desktopSearchInput.value = value;
}
if (mobileSearchInput && event.target !== mobileSearchInput) {
mobileSearchInput.value = value;
}
// Clear existing timer
if (searchDebounceTimer) {
clearTimeout(searchDebounceTimer);
}
// Apply filters immediately for UI feedback
applyFilters(true); // Skip URL update for now
// Use replaceState immediately so URL reflects current state
updateURL(true);
// After user stops typing, create a proper history entry
searchDebounceTimer = setTimeout(function() {
updateURL(false); // This creates a new history entry
}, 1000);
}
if (desktopSearchInput) {
desktopSearchInput.addEventListener('input', handleSearchInput);
}
if (mobileSearchInput) {
mobileSearchInput.addEventListener('input', handleSearchInput);
}
window.smrHandleSortChange = function() {
applyFilters();
};
var rangeInputs = ['smrOutletTempMin', 'smrOutletTempMax', 'smrThermalMin', 'smrThermalMax', 'smrGrossMin', 'smrGrossMax'];
rangeInputs.forEach(function(id) {
var input = document.getElementById(id);
input.addEventListener('input', applyFilters);
input.addEventListener('blur', function() {
var value = input.value.trim();
if (value === '' || isNaN(Number(value))) {
if (id === 'smrOutletTempMin') {
input.value = absoluteRanges.outletTemp.min;
} else if (id === 'smrOutletTempMax') {
input.value = absoluteRanges.outletTemp.max;
} else if (id === 'smrThermalMin') {
input.value = absoluteRanges.thermal.min;
} else if (id === 'smrThermalMax') {
input.value = absoluteRanges.thermal.max;
} else if (id === 'smrGrossMin') {
input.value = absoluteRanges.gross.min;
} else if (id === 'smrGrossMax') {
input.value = absoluteRanges.gross.max;
}
applyFilters();
return;
}
var numValue = Number(value);
if (id === 'smrOutletTempMin' || id === 'smrOutletTempMax') {
if (numValue < absoluteRanges.outletTemp.min) {
input.value = absoluteRanges.outletTemp.min;
} else if (numValue > absoluteRanges.outletTemp.max) {
input.value = absoluteRanges.outletTemp.max;
}
} else if (id === 'smrThermalMin' || id === 'smrThermalMax') {
if (numValue < absoluteRanges.thermal.min) {
input.value = absoluteRanges.thermal.min;
} else if (numValue > absoluteRanges.thermal.max) {
input.value = absoluteRanges.thermal.max;
}
} else if (id === 'smrGrossMin' || id === 'smrGrossMax') {
if (numValue < absoluteRanges.gross.min) {
input.value = absoluteRanges.gross.min;
} else if (numValue > absoluteRanges.gross.max) {
input.value = absoluteRanges.gross.max;
}
}
applyFilters();
});
});
function resetFilters() {
if (desktopSearchInput) desktopSearchInput.value = '';
if (mobileSearchInput) mobileSearchInput.value = '';
var allCheckboxes = document.querySelectorAll('#smrReactorTypeFilter input, #smrFuelEnrichmentFilter input, #smrSpectrumFilter input, #smrCountryFilter input, #smrDesignStatusFilter input, #smrApplicationsFilter input');
for (var i = 0; i < allCheckboxes.length; i++) {
allCheckboxes[i].checked = false;
}
document.getElementById('smrOutletTempMin').value = absoluteRanges.outletTemp.min;
document.getElementById('smrOutletTempMax').value = absoluteRanges.outletTemp.max;
document.getElementById('smrThermalMin').value = absoluteRanges.thermal.min;
document.getElementById('smrThermalMax').value = absoluteRanges.thermal.max;
document.getElementById('smrGrossMin').value = absoluteRanges.gross.min;
document.getElementById('smrGrossMax').value = absoluteRanges.gross.max;
applyFilters(false); // false = do update URL
}
var resetBtn = document.getElementById('smrResetBtn');
if (resetBtn) {
resetBtn.addEventListener('click', resetFilters);
}
var clearFiltersBtn = document.getElementById('smrClearFiltersBtn');
if (clearFiltersBtn) {
clearFiltersBtn.addEventListener('click', resetFilters);
}
// ---- URL State Management ----
// Serialize current state to URL parameters
function getStateFromFilters() {
var filters = getCurrentFilters();
var params = {};
// Search
if (filters.rawSearch) {
params.search = filters.rawSearch;
}
// Reactor types
if (filters.reactorTypes.length > 0) {
params.reactorType = filters.reactorTypes.join(',');
}
// Countries
if (filters.countries.length > 0) {
params.country = filters.countries.join(',');
}
// Design statuses
if (filters.designStatuses.length > 0) {
params.designStatus = filters.designStatuses.join(',');
}
// Fuel enrichments
if (filters.fuelEnrichments.length > 0) {
params.fuelEnrichment = filters.fuelEnrichments.join(',');
}
// Spectrums
if (filters.spectrums.length > 0) {
params.spectrum = filters.spectrums.join(',');
}
// NEW: Applications
if (filters.applications.length > 0) {
params.application = filters.applications.join(',');
}
// Ranges (only if not default)
if (filters.outletTempMin !== absoluteRanges.outletTemp.min) {
params.outletTempMin = filters.outletTempMin;
}
if (filters.outletTempMax !== absoluteRanges.outletTemp.max) {
params.outletTempMax = filters.outletTempMax;
}
if (filters.thermalMin !== absoluteRanges.thermal.min) {
params.thermalMin = filters.thermalMin;
}
if (filters.thermalMax !== absoluteRanges.thermal.max) {
params.thermalMax = filters.thermalMax;
}
if (filters.grossMin !== absoluteRanges.gross.min) {
params.grossMin = filters.grossMin;
}
if (filters.grossMax !== absoluteRanges.gross.max) {
params.grossMax = filters.grossMax;
}
// Sort order
var sortSelect = document.getElementById('smrSortSelect');
if (sortSelect && sortSelect.value !== 'name') {
params.sort = sortSelect.value;
}
return params;
}
// Update URL with current state
function updateURL(replaceState) {
var detailView = document.getElementById('smrDetailView');
var isDetailActive = detailView && detailView.classList.contains('active');
var params = new URLSearchParams();
// If detail view is active, just store the reactor name
if (isDetailActive) {
var titleEl = detailView.querySelector('.smr-detail-title');
if (titleEl) {
params.set('detail', titleEl.textContent);
}
} else {
// Store filter state
var state = getStateFromFilters();
for (var key in state) {
if (state.hasOwnProperty(key)) {
params.set(key, state[key]);
}
}
}
var newURL = window.location.pathname;
var paramString = params.toString();
if (paramString) {
newURL += '?' + paramString;
}
// Use pushState or replaceState
if (replaceState) {
history.replaceState(null, '', newURL);
} else {
history.pushState(null, '', newURL);
}
}
// Apply filters from URL parameters
function applyFiltersFromURL() {
var params = new URLSearchParams(window.location.search);
// Check if we're showing a detail view
var detailParam = params.get('detail');
if (detailParam) {
// Find and show the reactor detail
var reactor = reactors.find(function(r) { return r.name === detailParam; });
if (reactor) {
showReactorDetail(reactor.name, true);
return;
}
}
// If we were showing a detail view, hide it first
var detailView = document.getElementById('smrDetailView');
if (detailView && detailView.classList.contains('active')) {
hideReactorDetailDirect();
}
// Reset all filters first
if (desktopSearchInput) desktopSearchInput.value = '';
if (mobileSearchInput) mobileSearchInput.value = '';
var allCheckboxes = document.querySelectorAll('#smrReactorTypeFilter input, #smrFuelEnrichmentFilter input, #smrSpectrumFilter input, #smrCountryFilter input, #smrDesignStatusFilter input, #smrApplicationsFilter input');
for (var i = 0; i < allCheckboxes.length; i++) {
allCheckboxes[i].checked = false;
}
document.getElementById('smrOutletTempMin').value = absoluteRanges.outletTemp.min;
document.getElementById('smrOutletTempMax').value = absoluteRanges.outletTemp.max;
document.getElementById('smrThermalMin').value = absoluteRanges.thermal.min;
document.getElementById('smrThermalMax').value = absoluteRanges.thermal.max;
document.getElementById('smrGrossMin').value = absoluteRanges.gross.min;
document.getElementById('smrGrossMax').value = absoluteRanges.gross.max;
// Apply search
var searchValue = params.get('search');
if (searchValue) {
if (desktopSearchInput) desktopSearchInput.value = searchValue;
if (mobileSearchInput) mobileSearchInput.value = searchValue;
}
// Apply reactor types
var reactorTypeValue = params.get('reactorType');
if (reactorTypeValue) {
var types = reactorTypeValue.split(',');
types.forEach(function(type) {
var checkbox = document.querySelector('#smrReactorTypeFilter input[value="' + type + '"]');
if (checkbox) checkbox.checked = true;
});
}
// Apply countries
var countryValue = params.get('country');
if (countryValue) {
var countries = countryValue.split(',');
countries.forEach(function(country) {
var checkbox = document.querySelector('#smrCountryFilter input[value="' + country + '"]');
if (checkbox) checkbox.checked = true;
});
}
// Apply design statuses
var designStatusValue = params.get('designStatus');
if (designStatusValue) {
var statuses = designStatusValue.split(',');
statuses.forEach(function(status) {
var checkbox = document.querySelector('#smrDesignStatusFilter input[value="' + status + '"]');
if (checkbox) checkbox.checked = true;
});
}
// Apply fuel enrichments
var fuelValue = params.get('fuelEnrichment');
if (fuelValue) {
var fuels = fuelValue.split(',');
fuels.forEach(function(fuel) {
var checkbox = document.querySelector('#smrFuelEnrichmentFilter input[value="' + fuel + '"]');
if (checkbox) checkbox.checked = true;
});
}
// Apply spectrums
var spectrumValue = params.get('spectrum');
if (spectrumValue) {
var spectrums = spectrumValue.split(',');
spectrums.forEach(function(spectrum) {
var checkbox = document.querySelector('#smrSpectrumFilter input[value="' + spectrum + '"]');
if (checkbox) checkbox.checked = true;
});
}
// NEW: Apply applications
var applicationValue = params.get('application');
if (applicationValue) {
var apps = applicationValue.split(',');
apps.forEach(function(app) {
var checkbox = document.querySelector('#smrApplicationsFilter input[value="' + app + '"]');
if (checkbox) checkbox.checked = true;
});
}
// Apply ranges
if (params.has('outletTempMin')) {
document.getElementById('smrOutletTempMin').value = params.get('outletTempMin');
}
if (params.has('outletTempMax')) {
document.getElementById('smrOutletTempMax').value = params.get('outletTempMax');
}
if (params.has('thermalMin')) {
document.getElementById('smrThermalMin').value = params.get('thermalMin');
}
if (params.has('thermalMax')) {
document.getElementById('smrThermalMax').value = params.get('thermalMax');
}
if (params.has('grossMin')) {
document.getElementById('smrGrossMin').value = params.get('grossMin');
}
if (params.has('grossMax')) {
document.getElementById('smrGrossMax').value = params.get('grossMax');
}
// Apply sort
var sortValue = params.get('sort');
if (sortValue) {
var sortSelect = document.getElementById('smrSortSelect');
if (sortSelect) sortSelect.value = sortValue;
}
// Render with current state (don't update URL during popstate)
applyFilters(true);
}
// Handle browser back/forward
window.addEventListener('popstate', function() {
applyFiltersFromURL();
});
initializeFilters();
// Check if there are URL parameters and apply them, otherwise just render
if (window.location.search) {
applyFiltersFromURL();
} else {
applyFilters(true); // true = don't update URL on initial render
}
}, 100);
})();
