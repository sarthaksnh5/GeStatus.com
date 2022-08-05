$('#calendar').datepicker({
		});

!function ($) {
    $(document).on("click","ul.nav li.parent > a ", function(){          
        $(this).find('em').toggleClass("fa-minus");      
    }); 
    $(".sidebar span.icon").find('em:first').addClass("fa-plus");
}

(window.jQuery);
	$(window).on('resize', function () {
  if ($(window).width() > 768) $('#sidebar-collapse').collapse('show')
})
$(window).on('resize', function () {
  if ($(window).width() <= 767) $('#sidebar-collapse').collapse('hide')
})

$(document).on('click', '.panel-heading span.clickable', function(e){
    var $this = $(this);
	if(!$this.hasClass('panel-collapsed')) {
		$this.parents('.panel').find('.panel-body').slideUp();
		$this.addClass('panel-collapsed');
		$this.find('em').removeClass('fa-toggle-up').addClass('fa-toggle-down');
	} else {
		$this.parents('.panel').find('.panel-body').slideDown();
		$this.removeClass('panel-collapsed');
		$this.find('em').removeClass('fa-toggle-down').addClass('fa-toggle-up');
	}
})

let cho = 1;

function changecolor(){	
	var da = document.getElementsByClassName("far fa-dot-circle");

	if(cho == 1){
		for(let i = 0; i < da.length; i++){		
			da[i].style.color = "#f00";
		}
		cho = 2;
	}
	else if(cho == 2){
		for(let i = 0; i < da.length; i++){		
			da[i].style.color = "#808080";
		}
		cho = 3;
	}
	else{
		for(let i = 0; i < da.length; i++){		
			da[i].style.color = "#0f0";
		}
		cho = 1
	}
}

setInterval(changecolor, 500);

function getMacData(mac_id){
	var type1 = document.getElementById('dataType').value;
	var start = document.getElementById('startDate').value;
	var end = document.getElementById('endDate').value;

	// console.log(type1);
	// console.log(start);
	// console.log(end);

	var xmlhttp=new XMLHttpRequest();

	xmlhttp.onreadystatechange=function() {
		if (this.readyState==4 && this.status==200) {
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
			for(let i = 1; i < newData.length; i=i+2){
				dates.push(newData[i]);
			}
			let newInfo = [];
			for(let i = 0; i < newData.length; i=i+2){
				newInfo.push(newData[i]);
			}
			
			var lineChartData = {
				labels : dates,
				datasets : [
					{
						label: type1,
						fillColor : "rgba(48, 164, 255, 0.2)",
						strokeColor : "rgba(48, 164, 255, 1)",
						pointColor : "rgba(48, 164, 255, 1)",
						pointStrokeColor : "#fff",
						pointHighlightFill : "#fff",
						pointHighlightStroke : "rgba(48, 164, 255, 1)",
						data : newInfo
					}
				]
			}

			var chart1 = document.getElementById("line-chart").getContext("2d");
			window.myLine = new Chart(chart1).Line(lineChartData, {
			responsive: true,
			scaleLineColor: "rgba(0,0,0,.2)",
			scaleGridLineColor: "rgba(0,0,0,.05)",
			scaleFontColor: "#c5c7cc"
			});
			//window.alert(this.responseText);
		}
	}

	xmlhttp.open("GET","likeData/"+mac_id+"/"+type1+"/"+start+"/"+end,true);
	
	xmlhttp.send();
}

var opts = {
	angle: -0.19, // The span of the gauge arc
	lineWidth: 0.2, // The line thickness
	radiusScale: 1, // Relative radius
	pointer: {
		length: 0.56, // // Relative to gauge radius
		strokeWidth: 0.033, // The thickness
		color: '#000000' // Fill color
	},
	staticZones: [
		{strokeStyle: "#F03E3E", min: 0, max: 300}, // Red from 100 to 130
		{strokeStyle: "#FFDD00", min: 300, max: 600}, // Yellow
		{strokeStyle: "#30B32D", min: 600, max: 1800}, // Green
		{strokeStyle: "#FFDD00", min: 1800, max: 2400}, // Yellow
		{strokeStyle: "#F03E3E", min: 2400, max: 3000}  // Red
	],
	staticLabels: {
		font: "10px sans-serif",  // Specifies font
		labels: [0, 300, 600, 1800, 2400, 3000],  // Print labels at these values
		color: "#000000",  // Optional: Label text color
		fractionDigits: 0  // Optional: Numerical precision. 0=round off.
	},
	limitMax: false,     // If false, max value increases automatically if value > maxValue
	limitMin: false,     // If true, the min value of the gauge will be fixed
	colorStart: '#6FADCF',   // Colors
	colorStop: '#8FC0DA',    // just experiment with them
	strokeColor: '#E0E0E0',  // to see which ones work best for you
	generateGradient: true,
	highDpiSupport: true,     // High resolution support
	
	};
	var target = document.getElementById('rpm-gauge'); // your canvas element
	var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
	gauge.maxValue = 3000; // set max gauge value
	gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
	gauge.animationSpeed = 22; // set animation speed (32 is default value)
	gauge.set(975); // set actual value	

	var target = document.getElementById('oil-gauge'); // your canvas element
	var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
	gauge.maxValue = 3000; // set max gauge value
	gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
	gauge.animationSpeed = 22; // set animation speed (32 is default value)
	gauge.set(500); // set actual value	

	var target = document.getElementById('fuel-gauge'); // your canvas element
	var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
	gauge.maxValue = 3000; // set max gauge value
	gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
	gauge.animationSpeed = 22; // set animation speed (32 is default value)
	gauge.set(1500); // set actual value	

	var target = document.getElementById('xyz-gauge'); // your canvas element
	var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
	gauge.maxValue = 3000; // set max gauge value
	gauge.setMinValue(0);  // Prefer setter over gauge.minValue = 0
	gauge.animationSpeed = 22; // set animation speed (32 is default value)
	gauge.set(1500); // set actual value	
