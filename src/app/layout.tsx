import type { Metadata } from "next";
import { Inria_Sans } from "next/font/google";
import "../styles/globals.scss";

const inria = Inria_Sans({ subsets: ["latin"], weight: ["300", "400", "700"] });

export const metadata: Metadata = {
  title: "Telepathy",
  description: "I know what you're thinking",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inria.className}>{children}</body>
    </html>
  );
}
