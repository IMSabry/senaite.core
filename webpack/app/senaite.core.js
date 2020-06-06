import $ from "jquery";
import {i18n, _t, _p} from "./i18n-wrapper.js"


document.addEventListener("DOMContentLoaded", () => {
  console.debug("*** SENAITE CORE JS LOADED ***");

  // Initialize i18n message factories
  window.i18n = i18n;
  window._t = _t;
  window._p = _p;

  // BBB: set global `portal_url` variable
  window.portal_url = document.body.dataset.portalUrl

  // TinyMCE
  tinymce.init({
    selector: "textarea.mce_editable,div.ArchetypesRichWidget textarea,textarea[name='form.widgets.IRichTextBehavior.text'],textarea.richTextWidget",
    plugins: ["paste", "link", "autoresize", "fullscreen", "table", "code"],
    content_css : "/++plone++senaite.core.static/bundles/main.css",
  })
  // /TinyMCE


  // Sidebar
  var tid = null;
  $("#sidebar-header").on("click", function () {
    clearTimeout(tid)
    $("#sidebar").toggleClass("minimized");
  });
  $("#sidebar").on("mouseenter", function () {
    // delay sidebar expand 500ms
    tid = setTimeout(function(){
      $("#sidebar").removeClass("minimized");
    }, 1000);
    // console.debug("Setting sidebar timeout", tid);
  });
  $("#sidebar").on("mouseleave", function () {
    clearTimeout(tid)
    $("#sidebar").addClass("minimized");
    // console.debug("Clearing sidebar timeout", tid);
  });
  $("#sidebar ul li a").on("click", function () {
    clearTimeout(tid)
  });
  // /Sidebar


  // Tooltips
  $(function () {
    $("[data-toggle='tooltip']").tooltip()
  })
  // /Tooltips

});