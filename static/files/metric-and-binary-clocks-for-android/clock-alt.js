//var h_start = new Array(270,281.6,304.8,351.3,84.2);
//var h_ang = new Array(11.6,23.2,46.5,92.9,185.8);
//var m_start = new Array(270,275.7,287.1,310,355.7,87.1);
//var m_ang = new Array(5.7,11.4,22.9,45.7,91.4,182.9);
var h_start = new Array(270, 342, 54, 126, 198);
var h_ang = new Array(72,72,72,72,72);
var m_start = new Array(270, 330, 30, 90, 150, 210);
var m_ang = new Array(60,60,60,60,60,60);
var h_col = new jsColor();
var m_col = new jsColor();
var s_col = new jsColor();
var ctr = new jsPoint(600,300);
var t_ctr = new jsPoint(600,450);
var d = document;
var clock = new jsGraphics(d.getElementById("canvas"));
var h_rad = 250;
var m_rad = 200;
var s_rad = 160;

function bin(n) {
	var r = new Array();
    var i = 0;
    while (n > 0) {
        if (n % 2 == 1) {
            r[r.length]=i;
            n = n - 1;
		}
        n = n / 2;
        i++;
	}
    return r;
}

function updateClock(){
	clock.clear();
	var now = new Date();
	var hh = bin(now.getHours());
	var mm = bin(now.getMinutes());
	var ss = bin(now.getSeconds());
	for (var i=0;i<hh.length;i++){
		h_col.setRGB(0,(145-10*hh[i]),(250-10*hh[i]));
		var h_pen = new jsPen(h_col,20);
		clock.drawArc(h_pen,ctr,h_rad,h_rad,h_start[hh[i]],h_ang[hh[i]]);
	}
	for (var i=0;i<mm.length;i++){
		m_col.setRGB(10,(155-10*mm[i]),(250-10*mm[i]));
		var m_pen = new jsPen(m_col,15);
		clock.drawArc(m_pen,ctr,m_rad,m_rad,m_start[mm[i]],m_ang[mm[i]]);
	}
	for (var i=0;i<ss.length;i++){
		s_col.setRGB(30,(175-10*ss[i]),(250-10*ss[i]));
		var s_pen = new jsPen(s_col,10);
		clock.fillArc(s_col,ctr,s_rad,s_rad,m_start[ss[i]],m_ang[ss[i]]);
	}
	var min = now.getMinutes();
	if (min < 10){
		min = "0" + min
	}
	clock.drawText(now.getHours()+":"+min,t_ctr);
	setTimeout('updateClock()', 100);
}

updateClock();