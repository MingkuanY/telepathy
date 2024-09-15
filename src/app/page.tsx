"use client";

import { useEffect, useState } from "react";
import Header from "@/components/Header";
import styles from "../styles/home.module.scss";

export default function Home() {
  const [characters, setCharacters] = useState("Loading...");

  // Fetch the characters from Flask
  useEffect(() => {
    const fetchCharacters = async () => {
      try {
        const res = await fetch("http://localhost:4000/get_characters");
        const data = await res.json();
        setCharacters(data.characters);
      } catch (error) {
        setCharacters("Failed to load characters");
      }
    };

    // Set an interval to fetch updated characters every 2 seconds
    const interval = setInterval(fetchCharacters, 2000);

    // Clean up the interval when the component unmounts
    return () => clearInterval(interval);
  }, []);

  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.genContainer}>
        <p className={styles.sentence}>{characters}</p>
      </div>
    </div>
  );
}
