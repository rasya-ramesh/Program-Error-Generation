function calc_stats()
{
  document.getElementById("stats").style.display ="inline";
  var total_score=parseFloat("0.0");
  var num = 0;
  var c_count =0;
  var p_count =0;
  var c_score = 0;
  var p_score = 0;
  //gets table
  var oTable = document.getElementById('history_table');
  //gets rows of table
  var rowLength = oTable.rows.length;
  //loops through rows
  for (i = 0; i < rowLength; i++)
  {
     //gets cells of current row
     var oCells = oTable.rows.item(i).cells;
     //gets amount of cells of current row
     var cellLength = oCells.length;
     //Language wise
     var sc = parseFloat(oCells.item(3).innerHTML.substring(0, oCells.item(3).innerHTML.length - 1)) ;
     if(oCells.item(0).innerHTML.localeCompare("c")==0)
     {
       c_count+=1;
       c_score+=sc;
     }
     else if(oCells.item(0).innerHTML.localeCompare("python")==0)
     {
       p_count+=1;
       p_score+=sc;
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
   document.getElementById("avg").innerHTML = "Average Score :   "+total_score/num;
   p_score /= p_count;
   c_score /= c_count;
   var max,min;
   var max_score,min_score;
   if (p_count>c_count)
   {
     max="python";
     max_score = p_score;
     min="c";
     min = c_score;
   }
   else {

       max="c";
       max_score = c_score;
       min="python";
       min_score = p_score;
   }
   document.getElementById("s_lang").innerHTML = "Strongest Language  :  "+max + "   (Average score = " + max_score + "%)";
   document.getElementById("w_lang").innerHTML = "Weakest Language  :  "+min + "   (Average score = " + min_score + "%)";

   document.getElementById("tot_sub").innerHTML = "Total Submissions  :  "+ parseFloat(parseFloat(c_count)+parseFloat(p_count));
   document.getElementById("c_sub").innerHTML = "C Submissions  :  "+ c_count;
   document.getElementById("p_sub").innerHTML = "Python Submissions  :  "+ p_count;



}