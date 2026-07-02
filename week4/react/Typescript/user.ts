export interface User {
  results: {
    name: {
      first: string;
      last: string;
    };
    email: string;
    picture: {
      medium: string;
    };
  }[];
}

