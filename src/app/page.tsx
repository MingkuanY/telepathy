import Header from "@/components/Header";
import styles from "../styles/home.module.scss";

export default function Home() {
  const mock_data = "i know exactly what you're thinking...";

  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.genContainer}>
        <p className={styles.sentence}>{mock_data}</p>
      </div>
    </div>
  );
}
