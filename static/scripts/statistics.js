var c_count =0;
var p_count =0;
var c_score = 0;
var p_score = 0;
var times = [];
var scores =[];
var languages = [];
var categories = [];
var category_submissions = {};
var category_scores = {}
function calc_stats()
{
  document.getElementById("stats").style.display ="inline";
  var total_score=parseFloat("0.0");
  var num = 0;

  //gets table
  var oTable = document.getElementById('history_table');
  //gets rows of table
  var rowLength = oTable.rows.length;
  //loops through rows
  for (i = 0; i < rowLength; i++)
  {
     if(i!=0)
     {
       times.push(oTable.rows.item(i).cells[4].innerHTML);
       scores.push(oTable.rows.item(i).cells[3].innerHTML);
       languages.push(oTable.rows.item(i).cells[0].innerHTML);
       categories.push(oTable.rows.item(i).cells[1].innerHTML);

     }



     //gets cells of current row
     var oCells = oTable.rows.item(i).cells;
     //gets amount of cells of current row
     var cellLength = oCells.length;
     //Language wise
     var sc = parseFloat(oCells.item(3).innerHTML.substring(0, oCells.item(3).innerHTML.length - 1)) ;
     if(oCells.item(0).innerHTML.localeCompare("c")==0)
     {
       c_count+=1;
       if(!isNaN(sc))
      {
        c_score+=sc;
      }

     }
     else if(oCells.item(0).innerHTML.localeCompare("python")==0)
     {
       p_count+=1;
       if(!isNaN(sc))
       {
          p_score+=sc;
       }

     }

     //loops through each cell in current row
     for(var j = 0; j < cellLength; j++)
     {
        var cellVal = oCells.item(j).innerHTML;

        //Average score
        if(j==3)
        {
          var s = parseFloat(cellVal.substring(0, cellVal.length - 1)) ;
          if(!isNaN(s))
          {
              num+=1;
              total_score +=  s;
          }
        }

     }
   }

   document.getElementById("avg").innerHTML = "Average Score :   "+ (total_score/num).toFixed(2)+ "%";
   p_score /= p_count;
   c_score /= c_count;
   var max,min;
   var max_score,min_score;
   if (p_count>c_count)
   {
     max="python";
     max_score = p_score;
     min="c";
     min_score = c_score;
   }
   else {

       max="c";
       max_score = c_score;
       min="python";
       min_score = p_score;
   }
   document.getElementById("s_lang").innerHTML = "Strongest Language  :  "+max + "   (Average score = " + (max_score).toFixed(2) + "%)";
   document.getElementById("w_lang").innerHTML = "Weakest Language  :  "+ min + "   (Average score = " + (min_score).toFixed(2)+ "%)";

   document.getElementById("tot_sub").innerHTML = "Total Submissions  :  "+ parseFloat(parseFloat(c_count)+parseFloat(p_count));
   document.getElementById("c_sub").innerHTML = "C Submissions  :  "+ c_count;
   document.getElementById("p_sub").innerHTML = "Python Submissions  :  "+ p_count;

   display_chart();
   // bar_chart(p_score,c_score,"Average Scores");
   // bar_chart(p_count,c_count,"Submission counts");
}
function display_chart()
{
  // var ele = document.getElementsByName('radio');
  //
  // for(i = 0; i < ele.length; i++) {
  //     if(ele[i].checked)
  //       var selected = ele[i].value;
  // }
  //
bar_chart(p_score,c_score,"Average Scores");
bar_chart(p_count,c_count,"Submission counts");
time_chart();
categories_bar();
category_averages_chart();
  // if (selected =="as")
  // {
  //    bar_chart(p_score,c_score,"Average Scores");
  //
  // }
  // else if (selected =="sc"){
  //   bar_chart(p_count,c_count,"Submission counts");
  // }

  // else if (selected =="t"){
  //
  // }
}

function category_averages_chart()
{
    var dataPoints=[];
    //find average scores in each category
    for (var key in category_submissions)
    {
      //console.log(category_scores[key],category_submissions[key]);
      category_scores[key] = category_scores[key]/category_submissions[key];
      dataPoints.push ({y: category_scores[key], label:key});
      //console.log(category_scores[key]);
    }

    var chart = new CanvasJS.Chart("chartContainer5", {
      animationEnabled: true,
      title:{
        text:"Average Scores in Each Category"
      },
      axisX:{
        interval: 1,
        title : "Program categories"
      },
      axisY2:{
        interlacedColor: "rgba(129, 179, 155,.2)",
        gridColor: "rgba(129, 179, 155,.1)",
        interval:10
      },
      data: [{
        type: "bar",
        name: "companies",
        axisYType: "secondary",
        color: "#3d946b",
        dataPoints: dataPoints
      }]
    });


    chart.render();


}

function categories_bar()
{
      //populate category dictionaries
      for(var i =0 ; i<categories.length ; i++)
      {
        //console.log(parseFloat(scores[i].substring(0,scores[i].length -1)));
        if (categories[i] in category_submissions)
        {
          category_submissions[categories[i]] +=1;

          category_scores[categories[i]] += parseFloat(scores[i].substring(0,scores[i].length -1));
        }
        else {
          category_submissions[categories[i]]=1 ;
          category_scores[categories[i]] =  parseFloat(scores[i].substring(0,scores[i].length -1));
        }
      }
      var dataPoints =[]
      for (var key in category_submissions)
      {
        console.log(key, category_submissions[key]);
        dataPoints.push ({y: category_submissions[key], label:key});

      }

      var chart = new CanvasJS.Chart("chartContainer4", {
      	animationEnabled: true,
      	title:{
      		text:"Number of Submissions in Each Category"
      	},
      	axisX:{
      		interval: 1,
          title : "Program categories"
      	},
      	axisY2:{
      		interlacedColor: "rgba(117, 175, 191,.2)",
      		gridColor: "rgba(117, 175, 191,.1)",
      	  interval:1
      	},
      	data: [{
      		type: "bar",
      		name: "companies",
      		axisYType: "secondary",
      		color: "#014D65",
      		dataPoints: dataPoints
      	}]
      });
      chart.render();

}


function time_chart(){
      var pythontimes =[];
      var ctimes= [];
      for(var i =0; i<languages.length; i++)
      {
        if(languages[i] == "python")
        {
          pythontimes.push ( {label: times[i], y: parseFloat(scores[i].substring(0,scores[i].length -1)) } );
        }
        else {
          ctimes.push( {label: times[i], y:parseFloat(scores[i].substring(0,scores[i].length -1))} );
        }
      }

      var chart = new CanvasJS.Chart("chartContainer3", {
      	animationEnabled: true,
        theme: "light1",
      	title:{
      		text: "Performance over time"
      	},
      	axisX: {
          title: "Time",
          gridColor: "rgba(1,77,101,.06)",
      	},
      	axisY: {
      		title: "Score (in %)",
      		includeZero: true,
      		suffix: " %"
      	},
      	legend:{
      		cursor: "pointer",
      		fontSize: 16,
      		itemclick: toggleDataSeries
      	},
      	toolTip:{
      		shared: true
      	},
      	data: [{

      		name: "C",
      		type: "spline",
      		// yValueFormatString: "#0.## °C",
      		showInLegend: true,
      		dataPoints: ctimes

      	},
        {
      		name: "Python",
      		type: "spline",
      		// yValueFormatString: "#0.## °C",
      		showInLegend: true,
          dataPoints : pythontimes
      	}
      	]
      });
      chart.render();

      function toggleDataSeries(e){
      	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
      		e.dataSeries.visible = false;
      	}
      	else{
      		e.dataSeries.visible = true;
      	}
      	chart.render();
      }
}

function bar_chart(v1,v2,title){
      //delete chart;
      var cc;
      if( title ==  "Submission counts")
      {
         cc = "chartContainer1";
      }
      else
      {
        cc = "chartContainer2";
      }
      var chart = new CanvasJS.Chart(cc, {
         animationEnabled: true,
         exportEnabled: true,
         theme: "light2", // "light1", "light2", "dark1", "dark2"
         title:{
           text: title
       },
       data: [{
         type: "column", //change type to bar, line, area, pie, etc
         //indexLabel: "{y}", //Shows y value on all Data Points
         indexLabelFontColor: "#5A5757",
         indexLabelFontSize: 20,
         indexLabelPlacement: "outside",
         dataPoints: [
           { x: 10, y: parseInt(v1) , indexLabel: "\u2605 Python" },
           { x: 20, y: parseInt(v2), indexLabel: "\u2605 C"}

         ]
       }]
      });


      if( title ==  "Submission counts")
      {
         avg_score_chart = chart;
      }
      else
      {
        sc_chart = chart;
      }
      chart.render();

}


var server_addr="http://0.0.0.0:80";
function get_submissions()
{
  var route="/get_submissions"
  var data_file = server_addr+route;
  var http_request = new XMLHttpRequest();
  http_request.onreadystatechange = function() {//Call a function when the state changes.
      if(http_request.readyState == 4) {
          var response = JSON.parse(http_request.responseText);
          console.log(response)
          var table = document.getElementById("history_table");

          for(var key in response)
          {
            var u = document.getElementById("user");
            u.innerHTML = "User : "+response[key]["username"];
            console.log(key);
            var tr = document.createElement("tr");

            // var td2 = document.createElement("td");
            // td2.innerHTML = response[key]["cur_uname"];
            // tr.appendChild(td2);
            var td3 = document.createElement("td");
            td3.innerHTML = response[key]["language"];
            tr.appendChild(td3);
            var td4 = document.createElement("td");
            td4.innerHTML = response[key]["category"];
            tr.appendChild(td4);
            var td5 = document.createElement("td");
            td5.innerHTML = response[key]["program"];
            tr.appendChild(td5);
            var td6 = document.createElement("td");
            td6.setAttribute("class", "table_score")
            td6.innerHTML = response[key]["score"];
            tr.appendChild(td6);
            var td1 = document.createElement("td");
            td1.innerHTML = response[key]["datetime"];
            tr.appendChild(td1);
            table.appendChild(tr);

          }
      }
  }
  http_request.open('GET', data_file, true);
  http_request.send();
}
