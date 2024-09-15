"use client";

import { useEffect, useRef, useState } from "react";
import Header from "@/components/Header";
import styles from "../styles/home.module.scss";
import classnames from "classnames";

const actionCharacters = "WNJSCILA";

export default function Home() {
  const [characters, setCharacters] = useState("generating thoughts...");
  const [charStyle, setCharStyle] = useState(true);
  const containerRef = useRef<HTMLDivElement>(null); // Ref for the scrollable container

  // Gets most recent character, checks if it is an action, calls the corresponding script if action and displays the result on the frontend
  useEffect(() => {
    console.log("new character detected");
    if (characters.length >= 3 && characters.slice(-3) === "MOM") {
      console.log("authenticated");
      authenticated();
    }
    const mostRecentChar = characters[characters.length - 1];
    if (actionCharacters.includes(mostRecentChar)) {
      // If the most recent character is 'w', fetch the weather data
      if (mostRecentChar === "W") {
        console.log("new character is w");
        fetchWeatherData();
      } else if (mostRecentChar === "J") {
        console.log("new character is j");
        fetchJokeData();
      } else if (mostRecentChar === "S") {
        console.log("new character is s");
        fetchBankData();
      } else if (mostRecentChar === "N") {
        console.log("new character is n");
        fetchNewsData();
      }
    }
  }, [characters]);

  // Function to fetch weather data and play audio
  const fetchWeatherData = async () => {
    try {
      console.log("post request to w started");
      const res = await fetch("http://localhost:4000/w", {
        method: "POST",
      });
      const data = await res.json();
      console.log("post request to w ended");
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
  };

  // Function to fetch joke data and play audio
  const fetchJokeData = async () => {
    try {
      console.log("post request to j started");
      const res = await fetch("http://localhost:4000/j", {
        method: "POST",
      });
      const data = await res.json();
      console.log("post request to j ended");
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
  };

  // Function to fetch joke data and play audio
  const fetchBankData = async () => {
    try {
      console.log("post request to s started");
      const res = await fetch("http://localhost:4000/s", {
        method: "POST",
      });
      const data = await res.json();
      console.log("post request to s ended");
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
  };

  // Function to fetch joke data and play audio
  const fetchNewsData = async () => {
    try {
      console.log("post request to n started");
      const res = await fetch("http://localhost:4000/n", {
        method: "POST",
      });
      const data = await res.json();
      console.log("post request to n ended");
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
  };

  // Function to fetch joke data and play audio
  const authenticated = async () => {
    try {
      console.log("post request to a started");
      const res = await fetch("http://localhost:4000/a", {
        method: "POST",
      });
      const data = await res.json();
      console.log("post request to a ended");
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
  };

  // const renderContent = (char: string) => {
  //   switch (char) {
  //     case "w":
  //       return (
  //         <div className={styles.verticalContainer}>
  //           {/* <p className={styles.largeText}>
  //             72°F
  //           </p>
  //           <p className={styles.smallText}>
  //             Cambridge, Massachusetts
  //           </p> */}
  //           <p className={styles.smallText}>
  //             {weatherData && weatherData.summary}
  //           </p>
  //         </div>
  //       );
  //     case "j":
  //       return (
  //         <div className={styles.verticalContainer}>
  //           <p className={styles.smallText}>{jokeData?.joke}</p>
  //         </div>
  //       );
  //     case "Sign In":
  //       return <div>Sign In Successful</div>;
  //     case "Sign Out":
  //       return <div>Sign Out Successful</div>;
  //   }
  // };

  // Fetch the characters from Flask
  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const res = await fetch("http://localhost:4000/get_characters");
        const data = await res.json();
        setCharStyle(false);
        setCharacters(data.characters);
      } catch (error) {
        setCharacters("failed to telepathize");
      }
    };

    // Set an interval to fetch updated characters every 2 seconds
    const interval = setInterval(fetchCharacters, 2000);

    // Clean up the interval when the component unmounts
    return () => clearInterval(interval);
  }, []);

  // Auto-scroll when characters change
  useEffect(() => {
    const container = containerRef.current;
    if (container) {
      // Auto-scroll to the right with some margin
      container.scrollLeft = container.scrollWidth - container.clientWidth + 50;
    }
  }, [characters]);

  return (
    <div className={styles.main} ref={containerRef}>
      <Header />
      {/* {displayAction && (
        <div className={styles.dataDisplay}>
          {renderContent(characters[characters.length - 1])}
        </div>
      )} */}
      <div className={styles.genContainer}>
        <p
          className={classnames(
            styles.sentence,
            charStyle && styles.italicized
          )}
        >
          {characters}
        </p>
      </div>
    </div>
  );
}
