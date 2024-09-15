"use client";

import { useEffect, useRef, useState } from "react";
import Header from "@/components/Header";
import styles from "../styles/home.module.scss";
import classnames from "classnames";

export default function Home() {
  const [characters, setCharacters] = useState("generating thoughts...");
  const [charStyle, setCharStyle] = useState(true);
  const containerRef = useRef<HTMLDivElement>(null); // Ref for the scrollable container

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
