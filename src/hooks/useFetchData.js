import { useState, useEffect } from "react";
import { fetchData } from "../utils/api";

const useFetchData = (endpoint, action, body = null) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDataFromApi = async () => {
      setLoading(true);
      try {
        const result = await fetchData(endpoint, "POST", body);
        // Process the result based on the action type
        switch (action) {
          case "Weather":
            setData({
              long_text: result.long_text,
              summary: result.summary,
              audio_url: URL.createObjectURL(
                new Blob([result.audio_data], { type: "audio/mp3" })
              ),
            });
            break;
          case "Image":
            setData({
              image_url: result.image_url,
            });
            break;
          case "Sign In":
          case "Sign Out":
            setData({});
            break;
          // Add more cases as needed
          default:
            setData(result);
            break;
        }
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchDataFromApi();
  }, [endpoint, action, body]);

  return { data, error, loading };
};

export default useFetchData;
