import React, { createContext, useState } from "react";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";
import { Home } from "./Home";
import { Login } from "./Login";
import Map from "./Map";
import { Navbar } from "./Navbar";
import { AppContainer } from "./styles/AppContainer.css";
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  createHttpLink,
  gql,
} from "@apollo/client";
import { useCookies } from "react-cookie";
import jwt_decode from "jwt-decode";
import { Profile } from "./Profile";
import { Register } from "./Register";
import { UserProjects } from "./UserProjects";
import { CircularProgress } from "@mui/material";

type User = {
  id: number;
  email: string;
};

export const UserContext = createContext({
  authed: false,
  user: { id: 0, email: "" } as User,
});

export default function App() {
  const [loading, setLoading] = useState(true);
  const [isConnected, setIsConnected] = useState(false);
  const [cookies] = useCookies(["react-flask-app"]);

  const decoded: { user: User } = !!cookies?.["react-flask-app"]
    ? jwt_decode(cookies?.["react-flask-app"])
    : { user: { id: 0, email: "" } };
  const connectedUser = decoded?.user;

  const link = createHttpLink({
    uri: "/graphql",
    credentials: "include",
  });

  const client = new ApolloClient({
    uri: "http://localhost:5000/graphql",
    cache: new InMemoryCache(),
    link,
  });

  client
    .query({
      query: gql`
        query isConnected {
          isConnected {
            success
            errors
            user {
              id
              email
            }
          }
        }
      `,
    })
    .then((res) => {
      console.log(res);
      if (res.data.isConnected.success) setIsConnected(true);
      setLoading(false);
    });

  if (loading) {
    return (
      <div
        style={{
          display: "flex",
          height: "100vh",
          width: "100vw",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <CircularProgress />
      </div>
    );
  } else {
    return (
      <ApolloProvider client={client}>
        <UserContext.Provider
          value={{ authed: isConnected, user: connectedUser }}
        >
          <AppContainer className="App">
            <BrowserRouter>
              <Navbar />
              <Switch>
                <Route exact path="/">
                  <Home />
                </Route>
                <Route path="/map">
                  <Map />
                </Route>
                <Route path="/login">
                  <Login />
                </Route>
                <Route path="/profile">
                  <Profile />
                </Route>
                <Route path="/register">
                  <Register />
                </Route>
                <Route path="/myprojects">
                  <UserProjects />
                </Route>
                <Route render={() => <Redirect to="/"></Redirect>} />
              </Switch>
            </BrowserRouter>
          </AppContainer>
        </UserContext.Provider>
      </ApolloProvider>
    );
  }
}
