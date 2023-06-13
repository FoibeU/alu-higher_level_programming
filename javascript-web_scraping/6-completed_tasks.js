#!/usr/bin/node
const requests = require('request');

function getCompletedTasks (data, userId) {
  let count = 0;
  data
    .filter((element) => element.userId === userId)
    .forEach((tasks) => {
      if (tasks.completed) {
        count++;
      }
    });
  return count;
}

const url = process.argv[2];

const result = {};
requests.get(url, (error, results) => {
  if (error) {
    throw error;
  }
  const data = JSON.parse(results.body);
  data.forEach((element) => {
    if (!(element.userId in result)) {
      if (getCompletedTasks(data, element.userId) > 0) {
        result[element.userId] = getCompletedTasks(data, element.userId);
      }
    }
  });
  console.log(result);
});
