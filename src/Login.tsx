import React from 'react'
import { UserContext } from './App'
import { LoginContainer } from './styles/LoginContainer.css'

export const Login = () => {
  return (
    <UserContext.Consumer>
      {value => {
        if (value.email) {
          window.location.replace('/home')
        } else {
          return (
            <LoginContainer>Login</LoginContainer>
          )
        }
      }}
    </UserContext.Consumer>
  )
}
