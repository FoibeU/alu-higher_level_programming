exports.esrever = function (list) {
  const resList = [];

  for (let J = list.length - 1; J >= 0; J--) {
    const Index = list[J];
    resList.push(Index);
  }
  return resList;
};
