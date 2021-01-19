function dateStamp() {
    let newDate = new Date()
    // console.log('date', date)
    let year = newDate.getFullYear()
    let month = monthNumberToString(newDate.getMonth())
    let day = newDate.getDate()
    return month + " " + day + ', ' + year
  }
  
  function monthNumberToString(month){
      if (month === 0) {
          return "Jan"
      } else if (month === 1) {
          return "Feb"
      } else if (month === 2) {
          return "March"
      } else if (month === 3) {
          return "April"
      } else if (month === 4) {
          return "May"
      } else if (month === 5) {
          return "Jun"
      } else if (month === 6) {
          return "July"
      } else if (month === 7) {
          return "Aug"
      } else if (month === 8) {
          return "Sept"
      } else if (month === 9) {
          return "Oct"
      } else if (month === 10) {
          return "Nov"
      } else if (month === 11) {
          return "Dec"
      }
  }