function numbersOnly(array)
{
  var arr = array;
  var newArray = [];
  for(i = 0; i < arr.length; i++)
  {
    if(typeof arr[i] === "number")
    {
      newArray.push(arr[i])
    }
  }
  return newArray;
}
