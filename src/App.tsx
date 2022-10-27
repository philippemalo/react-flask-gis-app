import React, { createContext, useState } from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { Home } from "./Home";
import { Navbar } from "./Navbar";
import { AppContainer } from "./styles/AppContainer.css";
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  createHttpLink,
} from "@apollo/client";
import { useCookies } from "react-cookie";
import jwt_decode from "jwt-decode";
import { isConnectedQueryDocument } from "./graphql-types/queries";
import { User } from "./gql/graphql";
import { Loader } from "./Loader";

export const UserContext = createContext({
  authed: false,
  user: { id: "", email: "" } as User,
});

export default function App() {
  const [loading, setLoading] = useState(true);
  const [isConnected, setIsConnected] = useState(false);
  const [cookies] = useCookies(["react-flask-app"]);

  const decoded: { user: User } = !!cookies?.["react-flask-app"]
    ? jwt_decode(cookies?.["react-flask-app"])
    : { user: { id: "", email: "" } };
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

  client.query({ query: isConnectedQueryDocument }).then((res) => {
    if (res.data.isConnected?.success) setIsConnected(true);
    setLoading(false);
  });

  const Map = React.lazy(() => import("./Map"));
  const Login = React.lazy(() => import("./Login"));
  const Profile = React.lazy(() => import("./Profile"));
  const Register = React.lazy(() => import("./Register"));
  const UserProjects = React.lazy(() => import("./UserProjects"));
  const UserModels = React.lazy(() => import("./UserModels"));
  const Project = React.lazy(() => import("./Project"));

  if (loading) {
    return <Loader />;
  } else {
    return (
      <ApolloProvider client={client}>
        <UserContext.Provider
          value={{ authed: isConnected, user: connectedUser }}
        >
          <AppContainer className="App">
            <BrowserRouter>
              <Navbar />
              <Routes>
                <Route path="/" element={<Home />} />
                {/* <Route
                  path="/map"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <Map />
                    </React.Suspense>
                  }
                /> */}
                <Route
                  path="/login"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <Login />
                    </React.Suspense>
                  }
                />
                <Route
                  path="/profile"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <Profile />
                    </React.Suspense>
                  }
                />
                <Route
                  path="/register"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <Register />
                    </React.Suspense>
                  }
                />
                <Route
                  path="/myprojects"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <UserProjects />
                    </React.Suspense>
                  }
                />
                <Route
                  path="/myprojects/:projectid"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <Project />
                    </React.Suspense>
                  }
                />
                <Route
                  path="/mymodels"
                  element={
                    <React.Suspense fallback={<>...</>}>
                      <UserModels />
                    </React.Suspense>
                  }
                />
                <Route path="*" element={<Navigate replace to="/" />} />
              </Routes>
            </BrowserRouter>
          </AppContainer>
        </UserContext.Provider>
      </ApolloProvider>
    );
  }
}
