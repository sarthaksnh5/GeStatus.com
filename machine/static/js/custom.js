$("#calendar").datepicker({});

!(function ($) {
  $(document).on("click", "ul.nav li.parent > a ", function () {
    $(this).find("em").toggleClass("fa-minus");
  });
  $(".sidebar span.icon").find("em:first").addClass("fa-plus");
})(window.jQuery);
$(window).on("resize", function () {
  if ($(window).width() > 768) $("#sidebar-collapse").collapse("show");
});
$(window).on("resize", function () {
  if ($(window).width() <= 767) $("#sidebar-collapse").collapse("hide");
});

$(document).on("click", ".panel-heading span.clickable", function (e) {
  var $this = $(this);
  if (!$this.hasClass("panel-collapsed")) {
    $this.parents(".panel").find(".panel-body").slideUp();
    $this.addClass("panel-collapsed");
    $this.find("em").removeClass("fa-toggle-up").addClass("fa-toggle-down");
  } else {
    $this.parents(".panel").find(".panel-body").slideDown();
    $this.removeClass("panel-collapsed");
    $this.find("em").removeClass("fa-toggle-down").addClass("fa-toggle-up");
  }
});

let cho = 1;

function changecolor() {
  var da = document.getElementsByClassName("far fa-dot-circle");
  for (let i = 0; i < da.length; i++) {
    da[i].style.color = "#0f0";
  }
  // if(cho == 1){
  // 	for(let i = 0; i < da.length; i++){
  // 		da[i].style.color = "#f00";
  // 	}
  // 	cho = 2;
  // }
  // else if(cho == 2){
  // 	for(let i = 0; i < da.length; i++){
  // 		da[i].style.color = "#808080";
  // 	}
  // 	cho = 3;
  // }
  // else{
  // 	for(let i = 0; i < da.length; i++){
  // 		da[i].style.color = "#0f0";
  // 	}
  // 	cho = 1
  // }
}

// setInterval(changecolor, 500);
changecolor();

function getMacData(mac_id) {
  var type1 = document.getElementById("dataType").value;
  var start = document.getElementById("startDate").value;
  var end = document.getElementById("endDate").value;

  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      //document.getElementById("weektable").innerHTML=this.responseText;
      var data1 = this.responseText;
      data1 = data1.replaceAll(")(", ",");
      data1 = data1.replaceAll(" ", "");
      data1 = data1.replaceAll(")", "");
      data1 = data1.replaceAll("(", "");
      data1 = data1.replaceAll("'", "");
      let newData = data1.split(",");
      //console.log(newData);
      let dates = [];
      for (let i = 1; i < newData.length; i = i + 2) {
        dates.push(newData[i]);
      }
      let newInfo = [];
      for (let i = 0; i < newData.length; i = i + 2) {
        newInfo.push(newData[i]);
      }

      var lineChartData = {
        labels: dates,
        datasets: [
          {
            label: type1,
            fillColor: "rgba(48, 164, 255, 0.2)",
            strokeColor: "rgba(48, 164, 255, 1)",
            pointColor: "rgba(48, 164, 255, 1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(48, 164, 255, 1)",
            data: newInfo,
          },
        ],
      };

      var chart1 = document.getElementById("line-chart").getContext("2d");
      window.myLine = new Chart(chart1).Line(lineChartData, {
        responsive: true,
        scaleLineColor: "rgba(0,0,0,.2)",
        scaleGridLineColor: "rgba(0,0,0,.05)",
        scaleFontColor: "#c5c7cc",
      });
      //window.alert(this.responseText);
    }
  };

  xmlhttp.open(
    "GET",
    "likeData/" + mac_id + "/" + type1 + "/" + start + "/" + end,
    true
  );

  xmlhttp.send();
}
