const theme =document.getElementsByClassName("toggle")[0];
theme.addEventListener("click",function(){document.body.classList.toggle("dark-theme");});
let items = [];
const item_list = document.getElementsByClassName("list")[0];
item_list.addEventListener("click",function(){let value = document.getElementById("item").value;items.push(value);renderitems();});
function renderitems(){
    let list = document.getElementById("itemlist");
    list.innerHTML="";
    items.forEach(function(items){
    let li = document.createElement("li");
    li.textContent =items;
    list.appendChild(li);
    });
}
const userBtn = document.getElementById("userBtn");

userBtn.addEventListener("click", function () {

    fetch("https://randomuser.me/api/")
        .then(res => res.json())
        .then(data => {

            const user = data.results[0];

            document.getElementById("userCard").innerHTML = `
                <img src="${user.picture.medium}" />
                <p><b>Name:</b> ${user.name.first} ${user.name.last}</p>
                <p><b>Email:</b> ${user.email}</p>
            `;
        })
        .catch(err => {
            console.log("Fetch error:", err);
            document.getElementById("userCard").textContent =
                "Failed to load data";
        });
});