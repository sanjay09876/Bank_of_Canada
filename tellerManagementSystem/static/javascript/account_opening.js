// document.getElementById("existingcx"
// ).addEventListener("click", function() {
//             document.getElementById("existingcx-form").style.display = "block";
//         });
//         document.getElementById("newcx"
// ).addEventListener("click", function() {
//             document.getElementById("newcx-form").style.display = "block";
//         });

let existingCustomer = document.getElementById("existingcx");
let newCustomer =  document.getElementById("newcx");

existingCustomer.addEventListener("click",function() {
  document.getElementById("existingcx-form").style.display = "block";
  document.getElementById("newcx-form").style.display = "none";}
);

newCustomer.addEventListener("click",function() {
  document.getElementById("existingcx-form").style.display = "none";
  document.getElementById("newcx-form").style.display = "block";}
);

