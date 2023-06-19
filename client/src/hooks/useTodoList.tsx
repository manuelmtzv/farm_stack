import axios from "axios";
import { useState } from "react";

export const useTodoList = async () => {
  const [data, setData] = useState([]);

  const response = await axios.get("http://localhost:8000/api/todo");

  console.log(response.data);

  setData(response.data);

  return {
    data,
  };
};
