
let check = (!window.navigator.onLine) ? "offline" : "online";
if (check == "offline") {
            alert("Do you want to End your Examination?");
            setTimeout(function() {
            window.location.href = "/";
          }, 20000);
        }


function convertMinutesToMilliseconds(minutes) {
  return minutes * 60 * 1000;
}

var today_date = new Date().getTime();
console.log("Date:", today_date);

var timeInMinutes = parseInt(document.getElementById("timer").getAttribute("time"), 10);
console.log("timeInMinutes:", timeInMinutes);

var storedCountDownTime = localStorage.getItem("countDownTime"); // Get the stored countdown time from local storage

var countDownTime; // This will be used to store the actual countdown time

// Check if stored countdown time exists and is valid (not expired)
if (storedCountDownTime && parseInt(storedCountDownTime) > today_date) {
  countDownTime = parseInt(storedCountDownTime);
} else {
  // Calculate the countdown time and store it in local storage for future use
  countDownTime = convertMinutesToMilliseconds(timeInMinutes) + today_date;
  localStorage.setItem("countDownTime", countDownTime);
}

// Update the count down every 1 second
var x = setInterval(function () {
  // Get the current date and time
  var now = new Date().getTime();
  // Find the distance between now and the count down time
  var distance = countDownTime - now;
  // Time calculations for hours, minutes, and seconds
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Convert hours and minutes to 2-digit format with leading zeros
  var formattedHours = hours.toString().padStart(2, '0');
  var formattedMinutes = minutes.toString().padStart(2, '0');
  var formattedSeconds = seconds.toString().padStart(2, '0');

  // Output the result in elements with class names "hours," "minutes," and "seconds"
  document.getElementById("hours").innerHTML = formattedHours;
  document.getElementById("minutes").innerHTML = formattedMinutes;
  document.getElementById("seconds").innerHTML = formattedSeconds;

  // If the count down is over, redirect to the thank you page
  if (distance < 0) {
    clearInterval(x);
    window.location.href = "/";
  }
}, 1000);


document.getElementById("end").addEventListener("click", function() 
        {
            alert("Do you want to End your Examination?");
            setTimeout(function() {
            window.location.href = "/";
          }, 2000); // 5000 milliseconds = 5 seconds
        });


// Submit & End Button
document.getElementById("submit-end").addEventListener("click", function() 
        {
            alert("Do you want to submit & end your Examination?");
            setTimeout(function() {
            window.location.href = "/";
        }, 50); // 5000 milliseconds = 5 seconds
        });

