let points = 85;

if (points < 0 || points > 100) {
    console.log("Ошибка ввода");
} else if (points >= 90) {
    console.log("5");
} else if (points >= 75) {
    console.log("4");
} else if (points >= 60) {
    console.log("3");
} else {
    console.log("2");
}