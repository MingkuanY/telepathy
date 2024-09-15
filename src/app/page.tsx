"use client";

import { useEffect, useRef, useState } from "react";
import Header from "@/components/Header";
import styles from "../styles/home.module.scss";
import classnames from "classnames";
import useFetchData from "../hooks/useFetchData";

type Action =
  | "Weather"
  | "News"
  | "Joke"
  | "Show Deposits"
  | "Create Deposits"
  | "Image"
  | "Covert LLM"
  | "Whois"
  | "Sign In"
  | "Sign Out";

export default function Home() {
  const [characters, setCharacters] = useState("generating thoughts...");
  const [charStyle, setCharStyle] = useState(true);
  const [action, setAction] = useState<Action>("Weather"); // Example action
  const data = useFetchData("/api/endpoint", action);
  const containerRef = useRef<HTMLDivElement>(null); // Ref for the scrollable container

  const renderContent = () => {
    switch (action) {
      case "Weather":
        return (
          <div className={styles.verticalContainer}>
            <p className={styles.largeText}>72°F</p>
            <p className={styles.smallText}>Cambridge, Massachusetts</p>
          </div>
        );
      case "Image":
        return (
          <div>
            <h1>Image</h1>
          </div>
        );
      case "Sign In":
        return <div>Sign In Successful</div>;
      case "Sign Out":
        return <div>Sign Out Successful</div>;
      // Handle other actions here
    }
  };

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
      <div className={styles.dataDisplay}>{renderContent()}</div>
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
