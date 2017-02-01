function slots(quarters)
{
  while(quarters > 0)
  {
    if(Math.trunc(Math.random()*100) === 7) //Can choose any number between 0 to 99 as each has a 100:1 chance
    {
      quarters += Math.trunc(Math.random()*51)+50;
      return quarters;
    }
    else
    {
      quarters--
    }
  }
  return 0;
}
