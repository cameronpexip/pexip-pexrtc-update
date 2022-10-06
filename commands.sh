 rm pexrtc.js
 gunzip pexrtc.js.gz
 echo -e "$password" | sudo -S mv /opt/pexip/share/web/static/webrtc/js/pexrtc.js /opt/pexip/share/web/static/webrtc/js/pexrtc.js.bak
 echo -e "$password" | sudo -S mv pexrtc.js /opt/pexip/share/web/static/webrtc/js/