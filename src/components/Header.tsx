import styles from "../styles/header.module.scss";

export default function Header() {
  const morse = [
    [1, 2, 2, 2, 2],
    [2, 2, 2, 2, 1],
    [2, 2, 2, 1, 1],
    [1, 1, 1, 1, 2],
  ];

  return (
    <div className={styles.logoContainer}>
      <p className={styles.telepathy}>telepathy</p>
      <div className={styles.morse}>
        {morse.map((line, index1) => {
          return (
            <div className={styles.line} key={index1}>
              {line.map((thing, index2) => (
                <div
                  className={thing === 1 ? styles.dot : styles.dash}
                  key={index2}
                ></div>
              ))}
            </div>
          );
        })}
      </div>
    </div>
  );
}
