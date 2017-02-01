function printRange(start,end,skip)
{
  for(var i = start; i < end; i = i+skip)
  {
    console.log(i);
  }
}
printRange(2,10,2);
