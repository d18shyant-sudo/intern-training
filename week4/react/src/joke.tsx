import React from "react";

type Joke = {
  setup: string;
  punchline: string;
};

type State = {
  joke: Joke | null;
};

class RandomJoke extends React.Component<Record<string, never>, State> {
  constructor(props: Record<string, never>) {
    super(props);

    this.state = {
      joke: null
    };
  }

  fetchJoke = (): void => {
    fetch("https://official-joke-api.appspot.com/random_joke")
      .then((res) => res.json())
      .then((data: Joke) => {
        this.setState({ joke: data });
      })
      .catch((err) => {
        console.error("Error fetching joke:", err);
      });
  };

  componentDidMount(): void {
    this.fetchJoke();
  }

  render(): React.ReactNode {
    return (
      <div style={{ padding: "20px" }}>
        <h2> Random Joke</h2>

        {this.state.joke && (
          <div>
            <p><b>Setup:</b> {this.state.joke.setup}</p>
            <p><b>Punchline:</b> {this.state.joke.punchline}</p>
          </div>
        )}

        <button onClick={this.fetchJoke}>
          Get Another Joke
        </button>
      </div>
    );
  }
}

export default RandomJoke;