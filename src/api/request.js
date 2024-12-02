import axios from "axios";

const baseUrl = "http://127.0.0.1:20000";

export const upload = async (link) => {
  const params = new URLSearchParams();
  params.append("link", link);

  const response = await axios.post(baseUrl + "/upload", params, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  return response;
};

export const getTranscript = async () => {
  const params = new URLSearchParams();
  params.append("raw", "False");

  const response = await axios.post(baseUrl + "/transcript", params, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
  return response.data;
};

export const getSummary = async () => {
  try {
    const response = await axios.get(baseUrl + "/summary");
    return response.data;
    // return response.data;
  } catch (error) {
    console.error("Error fetching summary:", error.response || error.message);
    throw error;
  }
};

export const getQuiz = async () => {
  try {
    const response = await axios.get(baseUrl + "/quiz");
    return response.data;
  } catch (error) {
    console.error("Error fetching quiz:", error.response || error.message);
    throw error;
  }
};
