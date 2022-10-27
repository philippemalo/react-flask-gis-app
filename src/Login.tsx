import { useLazyQuery } from "@apollo/client";
import { Button, TextField } from "@mui/material";
import React, { useState } from "react";
import { UserContext } from "./App";
import { userLoginQueryDocument } from "./graphql-types/queries";
import { LoginContainer } from "./styles/LoginContainer.css";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [userLogin] = useLazyQuery(userLoginQueryDocument);

  const handleLogin = () => {
    userLogin({ variables: { email: email, password: password } }).then(
      (res) => {
        res?.data?.userLogin?.success
          ? window.location.replace("/home")
          : console.log("wrong creds");
      }
    );
  };

  return (
    <UserContext.Consumer>
      {(value) => {
        if (value.authed) {
          window.location.replace("/home");
        } else {
          return (
            <LoginContainer>
              <TextField
                id="email"
                label="EMAIL"
                variant="outlined"
                onChange={(e) => setEmail(e.currentTarget.value)}
              ></TextField>
              <TextField
                id="password"
                label="PASSWORD"
                variant="outlined"
                type="password"
                onChange={(e) => setPassword(e.currentTarget.value)}
              ></TextField>
              <Button variant="contained" onClick={handleLogin}>
                Log in
              </Button>
              <Button variant="text" color="error" href="/register">
                No account? Sign up here
              </Button>
            </LoginContainer>
          );
        }
      }}
    </UserContext.Consumer>
  );
};

export default Login;
