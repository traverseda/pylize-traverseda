/* DHTML-Bibliothek */

var DHTML = 0, DOM = 0, MS = 0, NS = 0, OP = 0;
var counter = 0; var d;
var keymap = Array();
keymap[110] = 'next';
keymap[112] = 'prev';
keymap[116] = 'toc';
keymap[113] = 'quit';

function DHTML_init() {
    if (window.opera) {
        OP = 1;
    }
    if (document.getElementById) {
        DHTML = 1;
        DOM = 1;
    }
    if (document.all && !OP) {
        DHTML = 1;
        MS = 1;
    }
    if (window.navigator && window.screen && !DOM && !OP) {
        DHTML = 1;
        NS = 1;
    }
}

function getWindowHeight() {
    var windowHeight = 0;
    if (typeof(window.innerHeight) == 'number') {
        windowHeight = window.innerHeight;
    }
    else {
        if (document.documentElement && document.documentElement.clientHeight) {
            windowHeight = document.documentElement.clientHeight;
        }
        else {
            if (document.body && document.body.clientHeight) {
                windowHeight = document.body.clientHeight;
            }
        }
    }
    return windowHeight;
}

function setPosition() {
    if (document.getElementById) {
        var windowHeight = getWindowHeight();
        if (windowHeight > 0) {
            var verticalOffset = 0;
            var bodyElement = document.getElementById('body');
            var headerElement = document.getElementById('header');
            var contentElement = document.getElementById('content');
            var footerElement = document.getElementById('footer');
            var bodyHeight = bodyElement.offsetHeight;
            var headerHeight = headerElement.offsetHeight;
            var contentHeight = contentElement.offsetHeight;
            if (footerElement) {
                var footerHeight = footerElement.offsetHeight;
            } else {
                var footerHeight = 0;
            }
            var contentArea = windowHeight - (headerHeight + footerHeight);
            var contentTop = (contentArea/2 - contentHeight/2- verticalOffset);
            var footerTop = windowHeight - footerHeight;

            /* center the content area */
            if (contentArea - contentHeight - footerHeight > 0) {
                contentElement.style.position = 'relative';
                contentElement.style.top = contentTop + 'px';
            }
            else {
                contentElement.style.position = 'static';
            }

            /* stick footer to the bottom */
            if (footerElement && windowHeight - (bodyHeight) > 0) {
                footerElement.style.position = 'absolute';
                footerElement.style.top = footerTop + 'px';
            }
            else {
                footerElement.style.position = 'static';
            }
        }
    }
}

function getLinkByName(name) {
  e = document.links[name];
  if (e) {
    return e;
  } else if (MS) {
    return document.all[name]
  }
}

function initPage() {
    setPosition();
    window.onresize = function() {
        setPosition();
    }
    d = getDelayedElements();
    for (var i=0; i < d.length; i++) {
      d[i].style.visibility = "hidden";
    }
}

function getDelayedElements() {
    var body = document.getElementsByTagName("body")[0];
    var el = body.getElementsByTagName("*");
    var a = Array();
    for (i=0; i < el.length; i++) {
        if (el[i].className == "delayed" || el[i].name == "delayed") {
            a.push(el[i]);
        }
    }
    return a;
}

function showNextDelayed() {
    if (counter < d.length) {
        d[counter].style.visibility = "visible";
        counter++;
        return true;
    }
    else {
        return false;
    }
}

function openTOC() {
  if (screen.availWidth) {
    var width = screen.availWidth;
    var height = screen.availHeight;
  } else {
    var width = screen.width;
    var height = screen.height-50;
  }
  if (MS) {
    width = width - 10;
    height = height - (height*0.03);
  }
  window.open('toc.html', 'toc',
    'location=no,menubar=no,status=no,resizable=yes,scrollbars=yes,toolbar=no,'
    + 'width=' + width + ',height=' + height +
    ',top=0,left=0');
  return false;
}

function action_next() {
    if (!showNextDelayed()) {
        link = document.getElementById("link_next");;
        if (link) {
            window.location.href = link;
        } else {
            el = document.getElementsByTagName('link')
            for (i=0; i < el.length; i++) {
                if (el[i].getAttribute('rel') == "next") {
                    window.location.href = el[i].getAttribute('href');
                }
            }
        }
    }
}

function action_prev() {
    link = document.getElementById("link_prev");
    if (link) {
        window.location.href = link;
    } else {
      link = document.getElementById("link_toc");;
      if (link) {
        window.location.href = link;
      }
    }
}

function action_toc() {
    link = document.getElementById("link_toc");
    if (link) {
        window.location.href = link;
    }
}

function action_start() {
    link = document.getElementById("link_start");
    if (link) {
        window.location.href = link;
    }
}

function action_end() {
    link = document.getElementById("link_end");
    if (link) {
        window.location.href = link;
    }
}

function action_quit() {
    window.close();
}

function handleKey(event) {
    /* IE does not provide the event objects as an argumnet
    but provides the global window.event object instead
    NS4 provides an argument named 'event' to every
    event handler function. We obtain a reference to the
    event object of all three event models by the following line: */
    if (!event) event = window.event;

    // ignore key press when CTRL or ALT is pressed simultaneously
    if (event.altKey || event.ctrlKey) {
        if (NS) window.routeEvent(event);
        return true;
    } else if (event.modifiers) {
        if (event.modifiers & Event.ALT_MASK ||
          event.modifiers % Event.CONTROL_MASK ||
          event.modifiers & Event.META_MASK) {
            if (NS) window.routeEvent(event);
            return true;
        }
    }

    // determine which key was pressed
    if (event.keyCode) {
        // the IE way
        keycode = event.keyCode;
    } else if (event.which) {
        // the NS way
        keycode = event.which;
    }
    //alert("Key pressed! ASCII-value: " + keycode);

    if (keycode == '32') {
         var action = 'next';
    } else if (keycode == '8') {
        var action = 'prev';
    } else {
        var action = keymap[keycode];
    }
    try {
        eval("action_" + action + "();");
    } catch(exc) {
        window.routeEvent(event);
        return true;
    }

    return false;
}

DHTML_init();

if (MS) {
    document.onkeypress = handleKey;
} else if (DOM) {
    document.onkeypress = handleKey;
    window.captureEvents(Event.KEYPRESS);
}

