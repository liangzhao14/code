---
source: https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors/small-modular-reactor-smr-global-tracker
downloaded: 2026-03-24 23:57:14
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [nuclear power reactors](https://world-nuclear.org/information-library/nuclear-power-reactors) / [small-modular-reactors](https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors) / Small Modular Reactor (SMR) Global Tracker

nuclear power reactors

# Small Modular Reactor (SMR) Global Project Tracker

Updated Monday, 16 February 2026

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
// About tab layout matching original structure
'#about-content { position: relative; min-height: 100vh; }' +
'.smr-about-left { position: absolute; top: 0; left: 0; width: 280px; padding: 48px 32px; text-align: right; font-weight: 800; font-size: 16px; line-height: 1.3; color: #111827; }' +
'.smr-about-right { padding-left: calc(280px + 32px); padding-top: 48px; }' +
'.smr-about-right p { font-size: 16px; line-height: 1.6; color: #374151; }' +
'.smr-tab-content { position: relative; }' +
'#about-content::before { content: ""; position: absolute; top: 0; bottom: 0; left: 280px; width: 0; border-right: 1px solid #e5e7eb; pointer-events: none; }' +
'.smr-project-tracker-content { padding: 32px; }' +
'.tableauPlaceholder { width: 100%; margin: 0 auto; }' + +
'.smr-project-tracker-content h2 { font-size: 24px; font-weight: 600; color: #212529; margin-bottom: 16px; }' +
'.smr-project-tracker-content p { font-size: 16px; line-height: 1.6; color: #374151; text-align: left; }' +
// Mobile responsive styles
'@media (max-width: 768px) {' +
'.smr-tabs-wrapper { padding: 0 16px; }' +
'.smr-tab { padding: 12px 16px; font-size: 14px; }' +
'.smr-about-left { position: static; width: auto; padding: 16px 16px 8px; text-align: left !important; margin: 0 !important; display: block; }' +
'.smr-about-right { padding: 0 16px 16px; }' +
'#about-content::before { content: none; }' +
'.smr-project-tracker-content { padding: 16px; }' +
'.tableauPlaceholder { margin: 0; }' +
'}' +
'</style>' +
// Tab structure - About tab on left, Project Tracker on right (Project Tracker default)
'<div class="smr-tabs-wrapper">' +
'<div class="smr-tabs">' +
'<button class="smr-tab" data-tab="about">About</button>' +
'<button class="smr-tab active" data-tab="project-tracker">Project Tracker</button>' +
'</div>' +
'</div>' +
// Project Tracker tab content - default active with Tableau map
'<div class="smr-tab-content active" id="project-tracker-content">' +
'<div class="smr-project-tracker-content">' +
'<div class="tableauPlaceholder" id="viz1763725079996" style="position: relative">' +
'<noscript>' +
'<a href="#">' +
'<img alt="Dashboard 2" src="https://public.tableau.com/static/images/Sm/SmallModularReactorSMRGlobalMap3/Dashboard2/1\_rss.png" style="border: none" />' +
'</a>' +
'</noscript>' +
'<object class="tableauViz" style="display:none;">' +
'<param name="host\_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />' +
'<param name="embed\_code\_version" value="3" />' +
'<param name="site\_root" value="" />' +
'<param name="name" value="SmallModularReactorSMRGlobalMap3&#47;Dashboard2" />' +
'<param name="tabs" value="no" />' +
'<param name="toolbar" value="yes" />' +
'<param name="static\_image" value="https://public.tableau.com/static/images/Sm/SmallModularReactorSMRGlobalMap3/Dashboard2/1.png" />' +
'<param name="animate\_transition" value="yes" />' +
'<param name="display\_static\_image" value="yes" />' +
'<param name="display\_spinner" value="yes" />' +
'<param name="display\_overlay" value="yes" />' +
'<param name="display\_count" value="yes" />' +
'<param name="language" value="en-US" />' +
'</object>' +
'</div>' +
'</div>' +
'</div>' +
// About tab content - exact replication of original formatting with updated text
'<div class="smr-tab-content" id="about-content">' +
'<div class="smr-about-left">SMR Global Project Tracker</div>' +
'<div class="smr-about-right"><p>The Tracker provides a comprehensive and interactive overview of SMR projects under development worldwide. It includes more than 70 projects at various stages of progress, from initial site preparation through to operation, as well as over 50 key pre-project agreements and related developments.</p><br><p>Updated regularly, the Tracker offers detailed summaries of recent milestones and activities. Users can filter projects by development status, technology type, and reactor model to explore the evolving landscape of SMR deployment, with direct links to relevant World Nuclear News articles for each entry.</p><br><p>For information about SMR designs, please visit our <a href="https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors/small-modular-reactor-smr-design-database" target="\_blank" rel="noopener noreferrer">SMR Design Database</a>. The database provides a comprehensive record of the many SMR designs at various stages of development across the world.</p></div>' +
'</div>';
// Tab switching functionality
function initializeTabs() {
var tabs = document.querySelectorAll('.smr-tab');
var tabContents = document.querySelectorAll('.smr-tab-content');
tabs.forEach(function(tab) {
tab.addEventListener('click', function() {
var targetTab = this.getAttribute('data-tab');
// Remove active class from all tabs and contents
tabs.forEach(function(t) { t.classList.remove('active'); });
tabContents.forEach(function(tc) { tc.classList.remove('active'); });
// Add active class to clicked tab
this.classList.add('active');
// Show corresponding content
var targetContent = document.getElementById(targetTab + '-content');
if (targetContent) {
targetContent.classList.add('active');
}
});
});
}
// Initialize tabs after a short delay to ensure DOM is ready
setTimeout(function() {
initializeTabs();
// Initialize Tableau visualization
initializeTableau();
}, 100);
// Tableau initialization function
function initializeTableau() {
var divElement = document.getElementById('viz1763725079996');
if (divElement) {
var vizElement = divElement.getElementsByTagName('object')[0];
if (divElement.offsetWidth > 800) {
vizElement.style.width = '100%';
vizElement.style.maxWidth = '1800px';
vizElement.style.height = (divElement.offsetWidth \* 0.75) + 'px';
vizElement.style.maxHeight = '877px';
} else if (divElement.offsetWidth > 500) {
vizElement.style.width = '100%';
vizElement.style.maxWidth = '1800px';
vizElement.style.height = (divElement.offsetWidth \* 0.75) + 'px';
vizElement.style.maxHeight = '877px';
} else {
vizElement.style.width = '100%';
vizElement.style.height = '827px';
}
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz\_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);
}
}
})();
