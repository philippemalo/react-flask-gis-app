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

export const userModelsQueryDocument = graphql(`
  query userModelsQueryDocument($userId: ID!) {
    userModels(userId: $userId) {
      success
      errors
      models {
        id
        name
      }
    }
  }
`);

export const allModelsQueryDocument = graphql(`
  query allModelsQueryDocument {
    allModels {
      success
      errors
      models {
        id
        name
      }
    }
  }
`);

export const projectQueryDocument = graphql(`
  query projectQueryDocument($projectId: ID!) {
    project(projectId: $projectId) {
      success
      errors
      project {
        id
        name
        models {
          id
          featureCollection {
            id
            geometry {
              id
              type
              coordinates
            }
          }
          centerPoint
          rotation
        }
        featureCollection {
          id
          geometry {
            id
            type
            coordinates
          }
          type
          properties
        }
      }
    }
  }
`);
