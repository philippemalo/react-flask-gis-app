import { graphql } from "../gql/gql";

export const isConnectedQueryDocument = graphql(`
  query isConnectedQueryDocument {
    isConnected {
      success
      errors
      user {
        id
        email
      }
    }
  }
`);

export const userLoginQueryDocument = graphql(`
  query userLoginQueryDocument($email: String!, $password: String!) {
    userLogin(email: $email, password: $password) {
      success
      errors
      user {
        id
        email
      }
    }
  }
`);

export const userProjectsQueryDocument = graphql(`
  query userProjectsQueryDocument($userId: ID!) {
    userProjects(userId: $userId) {
      success
      errors
      projects {
        id
        name
      }
    }
  }
`);
