var money = .01;
for(var i = 1; i < 30; i++)
{
  money = money + .01*(Math.pow(2,i));
}
console.log(money);
