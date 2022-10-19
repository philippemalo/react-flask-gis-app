import { graphql } from "../gql/gql";

export const createUserMutationDocument = graphql(`
  mutation createUserMutationDocument($email: String!, $password: String!) {
    createUser(email: $email, password: $password) {
      success
      errors
      user {
        id
        email
      }
    }
  }
`);

export const createProjectMutationDocument = graphql(`
  mutation createProjectMutationDocument($projectName: String!, $userId: ID!) {
    createProject(projectName: $projectName, userId: $userId) {
      success
      errors
      project {
        id
        name
      }
    }
  }
`);
