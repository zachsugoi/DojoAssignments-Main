var HOUR = 7;
var MINUTE = 40;
var PERIOD = "PM";

if(MINUTE < 30)
{
  if(PERIOD == "AM")
  {
    console.log("It's just after",HOUR,"in the morning")
  }
  else
  {
    console.log("It's just after",HOUR,"in the evening")
  }
}
else
{
  if(PERIOD == "AM")
  {
    console.log("It's almost",HOUR+1,"in the morning")
  }
  else
  {
    console.log("It's almost",HOUR+1,"in the evening")
  }
}
