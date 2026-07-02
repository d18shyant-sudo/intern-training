import type { User } from "./user";

fetch("https://randomuser.me/api/")
  .then((res: Response) => res.json())
  .then((data: User) => {
    const user = data.results[0];

    console.log("Name:", user.name.first, user.name.last);
    console.log("Email:", user.email);
    console.log("Picture:", user.picture.medium);
  })
  .catch((err: Error) => {
    console.error("Fetch error:", err);
  });