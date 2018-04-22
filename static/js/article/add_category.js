    var obtn1 = document.getElementById('btn1');
    var obox1 = document.getElementById('settin-main');
    var obtn2 = document.getElementById('btn2');
    var obox2 = document.getElementById('settin-main2');
    var oban1 = document.getElementById('ban1');
    var oban2 = document.getElementById('ban2');

    obtn1.onclick = function () {
        obox1.style.display = 'block';
    };

    obtn2.onclick = function () {
      obox2.style.display = 'block';
    };

    oban1.onclick = function () {
        obox1.style.display = 'none';
    };

    oban2.onclick = function () {
        obox2.style.display = 'none';
    };







